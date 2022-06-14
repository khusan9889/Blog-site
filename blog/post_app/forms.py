#from xml.etree.ElementTree import Comment
from django import forms
from .models import Post, Category, Comment

#choices = [('hobby', 'hobby'), ('movie', 'movie') ,('coding', 'coding'),  ('sport', 'sport'), ('art', 'art'), ('music', 'music')]

#go through category list and add them into Dropdown field
choices = Category.objects.all().values_list('name', 'name')
choice_list=[]

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =('title', 'header_image', 'author', 'slug', 'category', 'content', 'snippet' ,'status',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of your post'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': ' ', 'id':'elder', 'type': 'hidden'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Url slug'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your snippet goes here...'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'snippet' ,'status',)
        #fields = '__all__ '


        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of your post'}),
            #'image': forms.ImageField,
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Url slug'}),
            #'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'updated_on': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write yur post here...'}),
            'created_on': forms.DateInput(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),

        }
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of your post'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Url slug'}),

        }

