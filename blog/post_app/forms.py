from django import forms
from .models import Post, Category

#choices = [('hobby', 'hobby'), ('movie', 'movie') ,('coding', 'coding'),  ('sport', 'sport'), ('art', 'art'), ('music', 'music')]

#go through category list and add them into Dropdown field
choices = Category.objects.all().values_list('name', 'name')
choice_list=[]

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =('title', 'author', 'slug', 'category', 'content', 'status',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of your post'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': ' ', 'id':'elder', 'type': 'hidden'}),
            #'image': forms.ImageField,T
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Url slug'}),
            #'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your post here...'}),
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
        


