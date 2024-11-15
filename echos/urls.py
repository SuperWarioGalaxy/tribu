from django.urls import path

import waves.views

from . import views

app_name = 'echos'

urlpatterns = [
    path('', views.echos_list, name='echos-list'),
    path('<int:pk>/', views.echo_detail, name='echos-detail'),
    path('add/', views.add_echo, name='add-echo'),
    path('<int:pk>/edit/', views.echo_edit, name='echo-edit'),
    path('<int:pk>/delete/', views.echo_delete, name='echo-delete'),
    path('<int:pk>/waves/', views.echo_waves, name='echo-waves'),
    path('<int:pk>/waves/add', waves.views.add_wave, name='add-wave'),
]
