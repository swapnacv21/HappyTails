from django.urls import path
from . import views

urlpatterns=[
    path('',views.shop_login),
    path('shop_home',views.shop_home),
    path('logout',views.shop_logout),
    path('add_pet',views.add_pet),
    path('register',views.register),
    # path('user_home',views.user_home),
]