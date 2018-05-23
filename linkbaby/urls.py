from django.urls import path

from .views import HomeView, event_create


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create', event_create, name='create'),
]
