
from django.shortcuts import render
from blog.models import Product
from django.contrib.auth.decorators import login_required


def home_view(request):
    context = {
        "posts" : Product.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about_view(request):
    return render(request, 'blog/about.html')


@login_required()
def about_view(request):
    return render(request, 'blog/about.html')
