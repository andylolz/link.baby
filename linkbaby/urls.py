from django.urls import path

from .views import HomeView, eventorganiser_create


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create', eventorganiser_create, name='create'),
]
