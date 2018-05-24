from collections import OrderedDict

from django import forms
from django.core.validators import validate_email
from betterforms.multiform import MultiModelForm

from .models import Host, Linkup, Linkee


class MultiEmailField(forms.CharField):
    def to_python(self, value):
        if not value:
            return []
        return [x.strip() for x in value.split('\n') if x.strip() != '']

    def validate(self, value):
        super().validate(value)
        for email in value:
            validate_email(email)


class LinkeesForm(forms.Form):
    linkees = MultiEmailField(widget=forms.Textarea)

    def save(self, commit=True):
        linkees = []
        for email in self.cleaned_data['linkees']:
            linkee = Linkee(email=email)
            if commit:
                linkee.save()
            linkees.append(linkee)
        return linkees


class LinkupMultiForm(MultiModelForm):
    form_classes = OrderedDict((
        ('host', forms.modelform_factory(Host, exclude=())),
        ('linkup', forms.modelform_factory(Linkup, exclude=('host',))),
        ('linkees', LinkeesForm),
    ))
