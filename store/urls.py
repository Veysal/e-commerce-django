from django.urls import path
from . import views

app_name = 'store' #Пространство имен

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('categories/', views.category_list, name='category_list'),
    path('category/<slug:category_slug>/', views.product_list_by_category, name='product_list_by_category'),
]