from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import LinkupMultiForm


class HomeView(TemplateView):
    template_name = 'home.html'


class LinkupView(FormView):
    template_name = 'linkup_create.html'
    form_class = LinkupMultiForm
    success_url = '/'

    def form_valid(self, form):
        host = form['host'].save()
        linkup = form['linkup'].save(commit=False)
        linkup.host = host
        linkup.save()
        linkees = form['linkees'].save(commit=False)
        for linkee in linkees:
            linkee.linkup = linkup
            linkee.save()

        linkup.send_welcome_emails()

        return super().form_valid(form)
