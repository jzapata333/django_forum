from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.


def index(request):
    # IF the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST)
        # IF the form is valid
        if form.is_valid():
            # Yes = save it
            form.save()

            # Redirect it to Home
            return HttpResponseRedirect('/')

        else:
            # No = Show Error
            return HttpResponseRedirect(form.errors.as_json())

    # Get all posts, limit = 20
    posts = Post.objects.all()[:20]

    # show
    return render(request, 'posts.html', {'posts': posts})


def delete(request, post_id):
    # Find post
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')


def edit(request, post_id):
    # Find post
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        else:
            return HttpResponseRedirect(post.errors.as_json())

    posts = Post.objects.all()[:20]
    # form = PostForm

    # show
    return render(request, 'edit.html', {'post': post})
