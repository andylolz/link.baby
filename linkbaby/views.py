from django.forms import modelform_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from django.apps import apps
# from django.core.mail import send_mail

from .models import EventOrganiser


class HomeView(TemplateView):
    template_name = 'home.html'


def eventorganiser_create(request):
    template_name = 'event_organiser_create.html'
    UserForm = modelform_factory(apps.get_model(settings.AUTH_USER_MODEL),
                                 fields=('email',))
    EventOrganiserForm = modelform_factory(EventOrganiser, exclude=('user',))
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        event_organiser_form = EventOrganiserForm(request.POST)
        if all((event_organiser_form.is_valid(), user_form.is_valid())):
            user = user_form.save()
            event_organiser = event_organiser_form.save(commit=False)
            event_organiser.user = user
            event_organiser.save()
            return HttpResponseRedirect('/')
    else:
        event_organiser_form = EventOrganiserForm()
        user_form = UserForm()

    forms = (event_organiser_form, user_form)
    return render(request, template_name, {'forms': forms})
