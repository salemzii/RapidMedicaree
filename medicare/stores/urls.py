from django.urls import path
from . import views


urlpatterns = [
    path('create-category', views.add_category, name='create-category'),
    path('category-list', views.category_list, name='category-list'),
    path('categoryupdate/<int:pk>/',views.categoryUpdate, name='categoryupdate'),
    path('add-product/', views.addProduct, name='addproduct'),
    path('update-profile/<int:id>/', views.updateProduct, name='update-product')

]
