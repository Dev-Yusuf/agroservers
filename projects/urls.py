from django.urls import path
from . import views


urlpatterns =[
    path('', views.projects, name="projects" ),
    path('project/<str:pk>/', views.project, name="project" ),
    path('create-project/', views.createproject, name="create-project"),
    path('update-project/<str:pk>/', views.updateproject, name = "update-project"),
    path('delete-project/<str:pk>/', views.deleteProject, name = "delete-project"),
    path('about/', views.about, name = "about"),
    path('agents/', views.agents, name = "agents"),
    path('team/', views.team, name = "team"),
    path('ComingSoon/', views.ComingSoon, name = "ComingSoon")
    
]