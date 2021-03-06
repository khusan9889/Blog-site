from django.urls import path
from .views import ShowProfilePageView, UserRegisterView, UserEditView, PasswordsChangeView,EditProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_views
from . import views

#DRF
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('edit_profile/', UserEditView.as_view(), name = 'edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name= 'registration/change-password.html')),
    path('password_success', views.password_success, name= 'password_success'),
    path('<int:pk>/profile', ShowProfilePageView.as_view(), name='show_profile_page' ),
    path('<int:pk>/edit-profile_page', EditProfilePageView.as_view(), name='edit_profile_page' ),
    path('create-profile_page/', CreateProfilePageView.as_view(), name='create_profile_page' ),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)