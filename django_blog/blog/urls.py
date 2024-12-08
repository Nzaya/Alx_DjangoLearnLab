from . import views
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),

    path('posts/', views.PostListView.as_view(), name='post_list'),  # List view for all posts
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  # Detail view for individual post
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),  # Create new post
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),  # Edit post
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'), # Update post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),  # Delete post

    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='edit_comment'),
    path('posts/<int:pk>/comments/<int:comment_pk>/edit/', views.CommentUpdateView.as_view(), name='edit_comment'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete_comment'),
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='new_comment'),

    # path('search/', views.search, name='search'),  # Search URL

    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='posts_by_tag'),
]
