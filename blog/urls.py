from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
   path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('' , include('post_app.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    
    path('posts/', include('post_app.urls')),
    #path('posts/', include('post.urls')),


]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

