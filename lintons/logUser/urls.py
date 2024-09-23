from django.urls import path
from . import views

urlpatterns = [
    path("", views.signup_view, name = 'signup'),
    path("add/", views.sign_up_cust, name='cust_add')
]