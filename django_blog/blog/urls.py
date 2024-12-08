from django import views
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),

    path('', views.PostListView.as_view(), name='post-list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('new/', views.PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-edit'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

]
