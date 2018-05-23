from django.forms import modelform_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
# from django.core.mail import send_mail

from .models import Event


class HomeView(TemplateView):
    template_name = 'home.html'


def event_create(request):
    template_name = 'event_create.html'
    EventForm = modelform_factory(Event, exclude=('user',))
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event_form.save()
            return HttpResponseRedirect('/')
    else:
        event_form = EventForm()

    return render(request, template_name, {'form': event_form})
