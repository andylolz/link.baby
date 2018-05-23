from django.forms import modelform_factory, inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
# from django.core.mail import send_mail

from .models import Linkup, Host


class HomeView(TemplateView):
    template_name = 'home.html'


def linkup_create(request):
    template_name = 'linkup_create.html'
    LinkupForm = modelform_factory(Linkup, exclude=('user',))
    OrganiserFormSet = inlineformset_factory(Host, Linkup,
                                             exclude=(), can_delete=False,
                                             min_num=1, max_num=1)
    if request.method == 'POST':
        linkup_form = LinkupForm(request.POST)
        if linkup_form.is_valid():
            linkup_form.save()
            return HttpResponseRedirect('/')
    else:
        # form = LinkupForm()
        form = None
        formset = OrganiserFormSet()

    return render(request, template_name, {'form': form, 'formset': formset})
