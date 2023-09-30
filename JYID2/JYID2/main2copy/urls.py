from django.urls import path
from . import views

urlpatterns = [
    path('setget', views.setget, name='getdata'),
    path('', views.index, name='index'),
    path('potom', views.potom, name='potom'),
    path('get_subjects', views.get_subjects, name='get_subjects'),
    path('get_mycaptca', views.get_mycaptca, name='get_mycaptca'),
    path('vivod/delete/<int:id>/', views.delete_record, name='delete_record'),
    path('vivod/edit/<int:id>/', views.edit, name='edit'),
    path('vivod/update/<int:id>/', views.update, name='update'),
]

