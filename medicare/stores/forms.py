from django import forms
from .models import Category, Product, Delivery


class CreateCategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name']


class CategoryUpdateForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'category']

