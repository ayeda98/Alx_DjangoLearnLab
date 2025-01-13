from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # For built-in login/logout views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Django's built-in login view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Django's built-in logout view
    path('profile/', views.profile, name='profile'),  # Profile management
]
