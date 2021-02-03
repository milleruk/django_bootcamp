from django.urls import path, re_path
from django.contrib import admin

from products.views import (
    #bad_view,
    search_view,
    product_create_view,
    product_detail_view,
    product_api_detail_view,
    product_list_view
)

urlpatterns = [
    #path('bad-view-dont-use/', bad_view),
    path('search/', search_view),
    path('products/', product_list_view),
    path('products/create/', product_create_view),
    path('products/<int:pk>/', product_detail_view),
    #path('products/1/', views.product_api_detail_view),
    re_path(r'api/products/(?P<pk>\d+)/', product_api_detail_view),
    #path('api/products/<int:id>/', views.product_detail_view),
    path('admin/', admin.site.urls),
    
]
