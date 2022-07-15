from audioop import reverse
from datetime import datetime
from unicodedata import category
from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
#EMAIL
from django.conf import settings
from django.core.mail import send_mail


# ====  DRF  ====
from rest_framework import generics
from . import serializers

#API view
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.PostSerializer
    

# ====     ====


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ["-created_on"]

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs["pk"])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")


class AddCategoryView(CreateView):
    model = Category
    template_name = "add_category.html"
    fields = "__all__"


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace("-", " "))
    return render(
        request,
        "categories.html",
        {"cats": cats.title().replace("-", " "), "category_posts": category_posts},
    )


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, "category_list.html", {"cat_menu_list": cat_menu_list})


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse("article-detail", args=[str(pk)]))


# class AddCommentView(CreateView):
#     model = Comment
#     form_class = CommentForm
#     template_name = "add_comment.html"
#     success_url = reverse_lazy("home")

#     def form_valid(self, form):
#         form.instance.post_id = self.kwargs["pk"]
#         return super().form_valid(form)


def AddComment(request, post_id):
    post = Post.objects.get(id = post_id)
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            author = post.author.email
            new_comment.save()
            send_mail('You have received feedback to your post!', 'Check it in our Blog-site in comments section.', 'k.khusan2003@gmail.com' , [author])
            return redirect('home')
        
    else:
        form = CommentForm()
        context = {"form":form}
        return render(request, "add_comment.html", context)
