from django import forms
from .models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content','date_posted']
        widgets = dict(title=forms.TextInput(attrs={'class': 'form-control'}),
                       content=forms.Textarea(attrs={'class': 'form-control','rows':'5'}),
                       date_posted=forms.DateInput(format='%Y-%m-%d',attrs={'class': 'form-control','type':'date'}))
