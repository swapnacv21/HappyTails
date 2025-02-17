from django.urls import path
from . import views

urlpatterns=[
    path('',views.shop_login),
    path('shop_home',views.shop_home),
    path('logout',views.shop_logout),
    path('add_pet',views.add_pet),
    path('register',views.register),
    path('edit_pet/<id>',views.edit_pet),
    # path('delete_product/<id>',views.delete_product),
    # path('user_home',views.user_home),
]