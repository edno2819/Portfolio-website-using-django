from django.urls import path

from . import views


urlpatterns =[

    path("", views.index, name="index"),
    path("cv", views.page_cv, name="curriculo"),
    path("blog", views.blog, name="blog"),

]