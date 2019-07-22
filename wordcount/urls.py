from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="wordcountHome"),
    path('about/', views.about, name="about"),
    path('count/', views.count, name="count"),
]
