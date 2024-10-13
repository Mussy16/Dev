

from  django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=225)
    email =   forms.EmailField()
    fon_number = forms.CharField(max_length=15)
    content = forms.CharField(widget=forms.Textarea)