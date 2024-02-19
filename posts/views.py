from django.shortcuts import render
from .models import Post
from django.http import HttpResponse


# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by("-date")
    context = {"posts": posts}
    return render(request, "posts/post_list.html", context)


def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    print("This is my first page:",post)
    return render(request, "posts/post_page.html",{"post":post})

    # return HttpResponse(slug)
