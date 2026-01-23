from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:product_id>/', views.detail, name='detail'),
    path('create-checkout-session/<int:product_id>/', views.create_checkout_session, name='create_checkout_session'),
    path('success/', views.payment_success_view, name='payment_success'),
    path('cancel/', views.payment_cancel_view, name='payment_cancel'),
    path('createProduct/', views.create_product, name='create_product'),
    path('editProduct/<int:product_id>/', views.edit_product, name='edit_product'),
    path('deleteProduct/<int:product_id>/', views.product_delete, name='delete_product'),
    path('productList/', views.product_list, name='product_list'),
]