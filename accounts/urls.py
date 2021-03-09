from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='accounts.home'),
    path('product/', views.product, name='accounts.product'),
    path('customer/', views.customer, name='accounts.customer'),
    path('customer/<int:pk>/detail', views.customerDetail, name='accounts.customer.detail'),

    path('order/create', views.createOrder, name='accounts.order.create'),
    path('order/<int:pk>/update', views.updateOrder, name='accounts.order.update'),
    path('order/<int:pk>/delete', views.deleteOrder, name='accounts.order.delete')
]
