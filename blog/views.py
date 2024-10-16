from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from django.views import generic
from .models import Post

# Create your views here.
# def my_blog(request):
#     return HttpResponse("Hello, Blog!")


class PostList(generic.ListView):
    model = Post # same as all()
    # generic view
    # queryset = Post.objects.all().order_by("-created_on") # show all authors and ordering posts
    # queryset = Post.objects.filter(author=2) # show second author / filter
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post}
        # "coder": "Diana S"},
    )

    
    

