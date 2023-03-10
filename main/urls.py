from django.urls import path, include

from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
    # path("v1/", views.v1, name="view 1")
    # path("start/", views.index, name="index")
]
