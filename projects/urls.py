from django.urls import path

from projects import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view/<int:id>/', views.view, name='show'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('create/', views.create, name='create'),
]
