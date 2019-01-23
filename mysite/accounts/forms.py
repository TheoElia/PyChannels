from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,Patron, Retailer


class PatronCreationForm(UserCreationForm):
    # username = forms.CharField(max_length=200,
    # widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})))

    class Meta(UserCreationForm.Meta):
        model = Patron
        fields = ('username', 'email','user_img')


class PatronChangeForm(UserChangeForm):
    class Meta:
        model = Patron
	#exclude = ['is_superuser']
        fields = ('username', 'email','password','user_img',)


class RetailerCreationForm(UserCreationForm):
    # username = forms.CharField(max_length=200,
    # widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})))

    class Meta(UserCreationForm.Meta):
        model = Retailer
        fields = ('username', 'first_name', 'last_name', 'email','phone')


class RetailerChangeForm(UserChangeForm):
    class Meta:
        model = Retailer
        fields = ('username', 'first_name', 'last_name','email' ,'phone')


class CustomUserCreationForm(UserCreationForm):
    # username = forms.CharField(max_length=200,
    # widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})))

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email' )
