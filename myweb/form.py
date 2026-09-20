from django import forms
from .models import product

class productForm(forms.ModelForm):
    class Meta:
        model=product
        fields= ['name','category','semester','condition','price','desc','image']