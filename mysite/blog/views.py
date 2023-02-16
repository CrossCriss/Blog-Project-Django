from django.shortcuts import render
from .models import Post
from django.http import Http404


def post_list(request):
    posts = Post.publised.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, id):
    try:
        post =Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404("Page not found!")
    
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})