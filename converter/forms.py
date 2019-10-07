from django import forms
import converter.converter_api as c

class ConverterForm(forms.Form):
    currency_from = forms.ChoiceField(label="from", choices=c.get_currencies_tuple())
    currency_to = forms.ChoiceField(label="to", choices=c.get_currencies_tuple())
    amount = forms.IntegerField(label='Amount')