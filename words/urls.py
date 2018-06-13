from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = 'words'
urlpatterns = [
    path('', views.get_words, name='query'),
]
