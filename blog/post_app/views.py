from audioop import reverse
from datetime import datetime
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_on']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form = EditForm
    template_name = 'update_post.html'
    fields = '__all__'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')