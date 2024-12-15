from rest_framework import viewsets, permissions
from rest_framework import generics
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly
from django.contrib.contenttypes.models import ContentType
from rest_framework import filters
from .models import Post, Like

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Get posts from users that the current user is following
        following_users = user.following.all()  # List of users the current user is following
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

class LikePostView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        # Ensure the user hasn't already liked the post
        if Like.objects.filter(user=request.user, post=post).exists():
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create the like
        Like.objects.create(user=request.user, post=post)
        
        # Create a notification
        notification = Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target_content_type=ContentType.objects.get_for_model(post),
            target_object_id=post.id
        )
        
        return Response({"detail": "Post liked successfully."}, status=status.HTTP_200_OK)


class UnLikePostView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Like.objects.all()

    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        like = Like.objects.filter(user=request.user, post=post)
        if not like.exists():
            return Response({"detail": "You haven't liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Remove the like
        like.delete()
        
        return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK)