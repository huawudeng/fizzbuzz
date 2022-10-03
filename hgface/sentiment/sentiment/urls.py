from django.urls import path
from . import views


urlpatterns = [
    path('', views.infer, name='infer'),
]