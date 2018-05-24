from django.urls import path

from .views import HomeView, LinkupView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create', LinkupView.as_view(), name='create'),
]
