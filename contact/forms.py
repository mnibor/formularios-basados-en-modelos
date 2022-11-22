from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        # fields = '__all__' # PARA MOSTRAR TODOS LOS CAMPOS
        fields = ['name', 'email', 'message', 'contact_type', 'subscription']