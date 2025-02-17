from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('order/', views.pizza_order, name='order'),
    path('checkout/', views.checkout, name='checkout'),
    path('confirmation/<int:order_id>/', views.confirmation, name='confirmation'),
    path('login_user/', views.login_user, name='login'),
    path('register_user/', views.register_user, name='register_user'),
    path('logout/', views.logout_user, name='logout'),
    path('list_orders/', views.list_orders, name='list_orders'),
]