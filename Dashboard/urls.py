from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('Senegal', views.Senegal, name='senegal'),
    path('Algerie', views.Algerie, name='algerie'),
    path('Burkina', views.Burkina, name='burkina'),
    path('congoBrazza', views.congoBrazza, name='congoBrazza'),
    path('congoKinshasa', views.congoKinshasa, name='congoKinshasa'),
    path('Egypte', views.Egypte, name='egypte'),
    path('Ivorycoast', views.Ivorycoast, name='ivorycoast'),
    path('Mali', views.Mali, name='mali'),
    path('Maroc', views.Maroc, name='maroc'),
    path('Nigeria', views.Nigeria, name='nigeria'),
    path('Togo', views.Togo, name='togo'),
    path('Tunisie', views.Tunisie, name='tunisie'),
    
    path('test', views.dashboard, name='test'),

   
]