from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("deniz", views.deniz, name="deniz"),
    path("david", views.david, name="david")
]