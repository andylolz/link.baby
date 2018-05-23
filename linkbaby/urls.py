from django.urls import path

from .views import HomeView, linkup_create


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create', linkup_create, name='create'),
]
