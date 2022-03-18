from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:query>",views.query),
    path("newpage", views.createPage),
    path("edit/<str:query>",views.editPage, name="edit"),
    path("random", views.randomPage)
]
