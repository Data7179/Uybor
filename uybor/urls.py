from django.contrib import admin
from django.urls import path
from .views import Uy_Get, Uy_Post


urlpatterns = [
    path('show/', Uy_Get.as_view()),
    path('add/', Uy_Post.as_view()),
]
