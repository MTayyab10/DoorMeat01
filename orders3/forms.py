from django import forms
from .models import Customer, Discount, Butcher


class CustomerChangeForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'mobile',
            'city', 'town',
            'animal', 'quantity',
            'time', 'heard'
        ]


class DiscountChangeForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = [
            'coupon'
        ]


class ButcherChangeForm(forms.ModelForm):
    class Meta:
        model = Butcher
        fields = [
            'mobile',
            'city', 'town',
            'experience',
            'speciality', 'time',
            'price', 'heard',
        ]
