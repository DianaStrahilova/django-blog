from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from .models import Post

# Create your views here.
# def my_blog(request):
#     return HttpResponse("Hello, Blog!")


class PostList(generic.ListView):
    model = Post # same as all()
    # generic view
    queryset = Post.objects.all().order_by("-created_on") # show all authors and ordering posts
    # queryset = Post.objects.filter(author=2) # show second author / filter

