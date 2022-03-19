from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from .models import Post
from .forms import PostForm
# Create your views here.


# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'post_list.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'



def add_post(request):
    template = 'add_post.html'
    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('post:home')
    context = {"form":form}

    return render(request, template , context)


def update_post(request , pk):
    template = 'update_post.html'
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect('post:home')

    context = {"form":form}

    return render(request, template , context)


