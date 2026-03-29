from django.shortcuts import render
from django.http import HttpResponse\

from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }


    return render(request, template_name="post_list.html", context=context)


def post_detail(request, HttpRequest, pk: int):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    return render(request, template_name="post_detail.html", context=context)

def author_post_list(request, HttpRequest, auhtor_pk : int):
    posts = Post.objects.filter(author__pk=author_pk)
    context = {
        'posts': posts
    }
    return render(request, template_name="author_post_list.html", context=context)
