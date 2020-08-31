from django.shortcuts import render
from .models import Page


# Create your views here.
def list(request):
    context = {
        'titles' : Page.objects.all(),
    }
    return render(request, 'list.html', context)


def detail(request, page_id):
    context = {
        'page' : Page.objects.get(id = page_id),
    }

    return render(request, 'detail.html', context)
