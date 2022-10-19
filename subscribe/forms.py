from django import forms
from subscribe.models import Subscribe

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'
        labels = {
            'first_name': 'Enter First Name:',
            'last_name': 'Enter Last Name:',
            'email': 'Enter Email:'
        }