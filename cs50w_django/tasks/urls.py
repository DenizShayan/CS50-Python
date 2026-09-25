from django.urls import path

from . import views

urlpatterns = [
    path("", view.index, name="index")  
    path("add", views.add, name="add")
]