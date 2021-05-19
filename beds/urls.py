from django.urls import path

from . import views

urlpatterns=[
     path('', views.index,name='index'),
     path('dashboard', views.dashboard, name='dashboard'),
     path('patient_registration/', views.patient_registration, name='patient_registration'),
     path('bedallocate/', views.bedallocate, name='bedallocate'),
     path('discharge/<int:id>', views.discharge, name='discharge'),
]
