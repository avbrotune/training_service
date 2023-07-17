from django.urls import include, path

from training.api.views import hello

urlpatterns = [
    path('hello', hello, name="hello"),
]
