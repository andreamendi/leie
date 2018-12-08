from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    # path('hola/<str:name>', views.hola, name = 'hola')
    path('product/detail/<int:product_id>',views.detail_product, name='details_product'),  
    path('product/create/',views.create_product, name='create_product'),   
    path('product/update/<int:product_id>', views.update_product, name='update_product'),  
    path('product/delate/<int:product_id>',views.delete_product, name='delete_product'),
    path('rent/create/',views.create_rent, name='create_rent'),         
]