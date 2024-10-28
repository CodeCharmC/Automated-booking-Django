from django.urls import path
from . import views

urlpatterns = [
   path('appointments/', views.get_appointments),
   path('appointments/new', views.create_appointment),
   path('appointments/<int:id>/update', views.update_appointment),
   path('appointments/<int:id>/delete', views.delete_appointment),
]
