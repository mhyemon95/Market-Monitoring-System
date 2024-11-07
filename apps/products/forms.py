from django import forms
from .models import Product

class ProductSearchForm(forms.Form):
    query = forms.CharField(label="Search", max_length=100, required=False)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'image']
