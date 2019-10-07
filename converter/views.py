from django.shortcuts import render

from django.http import HttpResponse
from .forms import ConverterForm

import converter.converter_api as c

def form_to_data(form):
    return {
        'currency_from' : form.cleaned_data['currency_from'],
        'currency_to' : form.cleaned_data['currency_to'],
        'amount' : form.cleaned_data['amount']
    }

def index(request):
    if request.method == 'POST':
        form = ConverterForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = ConverterForm()
    context = {'form': form}
    return render(request, 'converter/index.html', context)
    # return HttpResponse(c.get_currencies())