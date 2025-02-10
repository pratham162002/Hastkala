from django import forms
from .models import Customer ,  Payment,CustomerInfo, Transaction


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'mobile_number']  # Ensure these fields exist in the Customer model


class LoginForm(forms.Form):
    mobile_number = forms.CharField(max_length=15)


# =====================================================
