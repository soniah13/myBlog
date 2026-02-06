from django import forms
from .models import *

class BlogForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), 
                                    empty_label='Select and author')
    
    class Meta:
        model = Blog
        fields = ['title', 'text', 'image', 'author', 'published_date']

    