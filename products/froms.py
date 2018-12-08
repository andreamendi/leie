from django import forms
from .models import Product, Rent

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = (
            'name',
            'description',
            'quality',
            'brand',
            'taken',
            'categories',
            'price',
            )

class RentForm(forms.ModelForm):
    class Meta:
        model = Rent

        fields = (
            'user',
            'product',
            'score',
            'begin_day',
            'end_day',
            'comment',
            )