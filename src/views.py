from django.shortcuts import render
from books.models import *


def home_page(requests):
    context = {
        'books' : Book.objects.all(),
        'categories' : Category.objects.all()
    }
    return render(requests, 'home-page.html', context)


def books(requests):
    context = {
        'books' : Book.objects.all(),
        # 'categories' : Category.objects.all()
    }
    return render(requests, 'books.html', context)

def book_details(requests, *args, **kwargs):
    context = {
        'book' : Book.objects.get(id=kwargs['pk']),
        # 'categories' : Category.objects.all()
    }
    return render(requests, 'book-details.html', context)


def books_categories(requests, *args, **kwargs):
    context = {
        'books' : Book.objects.all().filter(categories__in=kwargs['pk']),
        # 'categories' : Category.objects.all()
    }
    return render(requests, 'books.html', context)


