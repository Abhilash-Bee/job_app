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
        error_messages = {
            'email': {
                'ValidationError': 'Email already exists.',
            }
        }
    
    def clean_email(self):
        data = self.cleaned_data['first_name']
        emails = [em.email for em in Subscribe.objects.all()]
        print(emails)
        if data in emails:
            raise forms.ValidationError("Email already exists")
        return data            