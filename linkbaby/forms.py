from email.utils import parseaddr
from collections import OrderedDict

from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from betterforms.multiform import MultiModelForm

from .models import Host, Linkup, Linkee


class MultiEmailField(forms.CharField):
    def to_python(self, value):
        if not value:
            return []
        lines = value.split('\n')
        addresses = []
        for idx, line in enumerate(lines):
            if line.strip() == '':
                continue
            address = parseaddr(line)
            addresses.append({
                'line_num': idx + 1,
                'name': address[0],
                'email': address[1],
            })
        return addresses

    def validate(self, value):
        super().validate(value)
        for line in value:
            try:
                validate_email(line['email'])
            except ValidationError:
                tmpl = 'Email address "{email}" is invalid (line {line_num}).'
                raise ValidationError(tmpl.format(
                    email=line['email'], line_num=line['line_num']))


class LinkeesForm(forms.Form):
    recipients = MultiEmailField(widget=forms.Textarea)

    def save(self, commit=True):
        linkees = []
        for line in self.cleaned_data['recipients']:
            linkee = Linkee(email=line['email'], name=line['name'])
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
