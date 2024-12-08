from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from .models import Comment
from taggit.forms import TagWidget  # Import TagWidget for custom tag input
from taggit.models import Tag

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Provide a valid email address.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email")

class PostForm(forms.ModelForm):
    # Add tags as a field in the form
    tags = forms.CharField(widget=TagWidget(), required=False)

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def clean_tags(self):
        tags = self.cleaned_data.get('tags')
        if tags:
            # If tags are provided, split them and create or get tags
            tags_list = [tag.strip() for tag in tags.split(',')]
            tags_objs = []
            for tag in tags_list:
                tag_obj, created = Tag.objects.get_or_create(name=tag)
                tags_objs.append(tag_obj)
            return tags_objs
        return []

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Add your comment...'}),
        }