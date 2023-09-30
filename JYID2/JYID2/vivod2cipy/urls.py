from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('datatable_data/', views.datatable_data, name='datatable_data'),
    path('setget', views.setget, name='getdata'),
]

