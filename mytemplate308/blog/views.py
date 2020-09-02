from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Post

### BLOG VIEWS ###


def index(request):
    lastest_posts = Post.objects.order_by('-created_at')[:5]
    # output = ', '.join([i.title for i in lastest_posts])
    # return HttpResponse(output)
    template = loader.get_template("blog/index.html")
    context = {'lastest_posts': lastest_posts}
    return HttpResponse(template.render(context, request))


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'lastest_posts'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.order_by('-created_at')[:5]


def detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404
    template = loader.get_template("blog/detail.html")
    context = {'post': post}
    return HttpResponse(template.render(context, request))


def detail_modern(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "blog/detail.html", {'post': post})


class DetailView(generic.DetailView):
    model = Post
    template_name = "blog/detail.html"


def create(request):
    return HttpResponse("create.")


def edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "blog/edit.html", {'post': post})

def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    try:
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return HttpResponseRedirect(reverse('blog:detail', args=(post.id,)))
    except:
        return render(request, 'blog/detail.html', {'post': post, 'error_message': 'some error!'})


def delete(request, post_id):
    return HttpResponse("delete id: %s" % post_id)
