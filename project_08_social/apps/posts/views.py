from django.shortcuts import get_object_or_404, redirect, render

from .models import Post
from .forms import PostForm,CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            
    else:
        form = PostForm(data=request.GET)
    return render(request, 'posts/create_post.html', {'form': form})

def feed(request):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False) # - builds a Comment object in memory. Do not commit yet
            new_comment.user = request.user
            post_id = request.POST.get('post_id')
            new_comment.post = get_object_or_404(Post,  id=post_id)
            new_comment.save()
    comment_form = CommentForm()
    posts = Post.objects.all()  
    logged_in_user = request.user
    return render(request, 'posts/feed.html', {'posts': posts, 'logged_in_user': logged_in_user, 'comment_form': comment_form})

def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    user = request.user
    if user in post.liked_by.all():
        post.liked_by.remove(user)
    else:
        post.liked_by.add(user)
    return redirect('feed') 