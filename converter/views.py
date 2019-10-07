from django.shortcuts import render

from django.http import HttpResponse
from .forms import ConverterForm

def form_to_context(form):
    return {
        'form': form,
        'currency_from' : form.cleaned_data['currency_from'],
        'currency_to' : form.cleaned_data['currency_to'],
        'amount' : form.cleaned_data['amount']
    }

def index(request):
    context = None
    if request.method == 'POST':
        form = ConverterForm(request.POST)
        if form.is_valid():
            # make request and get the data
            context = form_to_context(form)
            # send the new data to the context
    else:
        context = {'form': ConverterForm()}

    return render(request, 'converter/index.html', context)