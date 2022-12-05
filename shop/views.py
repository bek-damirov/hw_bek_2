from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item, Purchase


def index(request):
    list_item = Item.objects.all()
    context = {
        'list_item': list_item
    }
    return render(request, 'index.html', context)


def detail(request, id):
    item = get_object_or_404(Item, id=id)
    context = {
        'item': item,
    }
    return render(request, 'detail.html', context)
