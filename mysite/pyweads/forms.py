from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Product
from django.forms import ModelForm
from django.utils.safestring import mark_safe


class ProductCreationForm(ModelForm):
    # username = forms.CharField(max_length=200,
    # widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})))
    class Meta:
        model =Product
        fields = ('name','price','description','product_img1','product_img2','product_img3',)
    	
   
class ProductChangeForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name','price','product_img1','product_img2','product_img3','description')

