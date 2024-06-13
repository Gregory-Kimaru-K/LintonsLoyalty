from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginAdmin, name='loginAdmin'),
    path('pointadd/', views.pointAdd, name='pointAdd'),
    path('logout/', views.logout_view, name='logout')
]