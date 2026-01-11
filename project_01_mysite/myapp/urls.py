from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

app_name = 'myapp'

urlpatterns = [
    #path('', cache_page(60)(views.index),name='index'),
    path('', views.index,name='index'),
    # path('', views.IndexClassView.as_view(), name='index'),
    path('<int:item_id>/', views.detail,name= 'detail'), 
    # path('<int:pk>/', views.DetailClassView.as_view(),name= 'detail'), 
    # path('add/', views.create_item, name='create_item'),  
     path('add/', views.ItemCreateView.as_view(), name='create_item'),  
    #path('update/<int:item_id>/', views.update_item, name='update_item'),  
    path('update/<int:pk>/', views.ItemUpdateView.as_view(), name='update_item'),
    #path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('delete/<int:pk>/', views.DeleteItemView.as_view(), name='delete_item'),
]
