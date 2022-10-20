from re import sub
from xml.dom import ValidationErr
from django.shortcuts import render
from django import forms
from subscribe.forms import SubscribeForm

# Create your views here.
def subscribe_page(request):
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            submitted_form = form.instance
            return render(request, 'subscribe/email.html', context={'submitted_form': submitted_form})
    context = {
        'form': form,
    }
    return render(request, 'subscribe/email.html', context=context)    