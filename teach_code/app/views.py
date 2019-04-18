from django.shortcuts import render
from .models import CodeModel,Tag
from .forms import CodeModelForm,SearchForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    searchform = SearchForm
    codes = CodeModel.objects.all()
    context = {
    'searchform':searchform,
    'codes':codes,
    }
    if request.method == 'POST':
        str = request.POST['search']
        search_word = CodeModel.objects.filter(title__contains=str)
        context['search_word'] = search_word
    return render(request,'app/index.html',context)


def contribution(request):
    code_form = CodeModelForm
    context = {
        'code_form':code_form,
    }

    return render(request,'app/contribution.html',context)


def add(request):
    form = CodeModelForm(request.POST)
    form.save()
    return HttpResponseRedirect(reverse('index'))




def event(request,id):
    codes = CodeModel.objects.all().filter(id=id)

    context = {
    'codes':codes,
    }
    return render(request,'app/event.html',context)
