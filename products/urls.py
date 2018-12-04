from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    # path('hola/<str:name>', views.hola, name = 'hola')
    path('product/detail/<int:product_id>',views.detail_product, name='details_product')
]