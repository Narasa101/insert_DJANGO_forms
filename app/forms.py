from django import forms

class schoolform(forms.Form):
    name=forms.CharField(max_length=100)
    prinicipal=forms.CharField(max_length=100)
    location=forms.CharField(max_length=100)