from django import forms
from product_app.models import*
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = ProductUserModel
        fields = ['username','full_name','email','phone_number', 'password1','password2']

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'
        widgets = {
            'production_date': forms.DateInput(attrs={'type':'date'})
        }
        exclude = ['total_amount','created_by']