from unicodedata import name
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    #creator = ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=200, unique=True)
    header_image = models.ImageField(null=True, blank =True, upload_to ='images/')
    slug = models.SlugField(blank= True,max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    category = models.CharField(max_length=200, default='music')
    updated_on = models.DateTimeField(auto_now= True)
    content = RichTextField(blank=True, null=True)
    snippet = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_post')
    status = models.IntegerField(choices=STATUS, default=0)
    

    class Meta:
        ordering = ['-created_on']

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    
    def get_absolute_url(self):
        return reverse('home')


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank =True, upload_to ='images/profile')
    website_url = models.CharField(max_length=200, unique=True, null=True, blank =True)
    instagram_url = models.CharField(max_length=200, unique=True, null=True, blank =True)
    telegram_url = models.CharField(max_length=200, unique=True, null=True, blank =True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')