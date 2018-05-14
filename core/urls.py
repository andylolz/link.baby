from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path(r'', include('linkbaby.urls')),
    path('admin/', admin.site.urls),
]
