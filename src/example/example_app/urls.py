from django.urls import path
from .views import ThreeCitiesTimezone

app_name = 'example_app'
urlpatterns = [
    path('', ThreeCitiesTimezone.as_view(), name='index'),
]
