from django.urls import path

from . import views

app_name = 'echos'

urlpatterns = [
    path('', views.echos_list, name='echos-list'),
    path('<int:pk>/', views.echos_detail, name='echos-detail'),
    path('add/', views.add_echo, name='add-echo'),
    path('<int:pk>/edit/', views.echo_edit, name='echo-edit'),
    path('<int:pk>/delete/', views.echo_delete, name='echo-delete'),
]
