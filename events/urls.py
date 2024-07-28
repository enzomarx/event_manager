from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/<int:id>/', views.event_detail, name='event_detail'),
    path('register/<int:event_id>/', views.register_for_event, name='register_for_event'),
]
