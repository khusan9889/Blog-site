from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of your post'}),
            #'image': forms.ImageField,
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Url slug'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'updated_on': forms.DateInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write yur post here...'}),
            'created_on': forms.DateInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),

        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of your post'}),
            #'image': forms.ImageField,
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Url slug'}),
            #'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'updated_on': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write yur post here...'}),
            'created_on': forms.DateInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),

        }
        


