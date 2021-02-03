from django.urls import path, re_path
from django.contrib import admin

from products.views import (
    home_view,
    product_detail_view,
    product_api_detail_view,
    product_list_view
)

urlpatterns = [
    path('search/', home_view),
    path('products/', product_list_view),
    path('products/<int:pk>/', product_detail_view),
    #path('products/1/', views.product_api_detail_view),
    re_path(r'api/products/(?P<pk>\d+)/', product_api_detail_view),
    #path('api/products/<int:id>/', views.product_detail_view),
    path('admin/', admin.site.urls),
    
]
