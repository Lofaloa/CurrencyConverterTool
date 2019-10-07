from django import forms

class ConverterForm(forms.Form):
    currency_from = forms.CharField(label='From', max_length=100)
    currency_to = forms.CharField(label='To', max_length=100)
    amount = forms.IntegerField(label='Amount')