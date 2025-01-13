from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # For built-in login/logout views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Django's built-in login view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Django's built-in logout view
    path('profile/', views.profile, name='profile'),  # Profile management
    path('', views.PostListView.as_view(), name='post_list'),  # Liste des articles
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  # Détail d'un article
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),  # Création d'un article
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),  # Modification d'un article
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),  # Suppression d'un article
]
]
