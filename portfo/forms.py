
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('mame','email','body')
        widgets = {
            'mame': forms.TextInput(attrs={'class': 'form-control w-100 mx-4','placeholder': 'Enter name' }),
            'email': forms.TextInput(attrs={'class': 'form-control w-100 mx-4', 'placeholder': 'Enter email'}),
            'body': forms.Textarea(attrs={'class': 'form-control w-100 mx-4 text-center', 'placeholder': 'Leave your comment'}),
        }

