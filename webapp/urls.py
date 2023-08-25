from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('cv/', views.cv, name="cv"),
    path('projects/', views.projects, name="projects"),
    path('contact/', views.contact, name="contact"),
    path('game/', views.game, name="game"),
    path('digitaltwin/', views.digitaltwin, name="digitaltwin"),
    path('thesis/', views.thesis, name="thesis"),
    path('aspnetproject/', views.aspnetproject, name="aspnetproject"),
    path('currentproject/', views.currentproject, name="currentproject"),
]