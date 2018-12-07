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
