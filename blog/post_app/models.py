from unicodedata import name
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    #creator = ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(blank = True,upload_to = 'media', height_field=200, width_field=200)
    slug = models.SlugField(blank= True,max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    category = models.CharField(max_length=200, default='music')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    


    class Meta:
        ordering = ['-created_on']

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