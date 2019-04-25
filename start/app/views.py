from django.shortcuts import render,get_object_or_404
from .forms import TextForm
from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    posts = Post.objects.all()
    form = TextForm
    context = {
        'posts':posts,
        'form':form,
    }
    return render(request,'app/index.html',context)


def add(request):
    form = TextForm(request.POST)
    form.save()
    return HttpResponseRedirect(reverse('index'))


def delete(request,id=None):
    post = get_object_or_404(Post,pk=id)
    post.delete()
    return HttpResponseRedirect(reverse('index'))
