from django import forms


class HomeForm(forms.Form):
    select_app = forms.CharField(max_length=20)
    Region = forms.CharField()

