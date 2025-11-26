from django.shortcuts import render
from .models import Publisher

def books_view(request):
    publishers = Publisher.objects.all()
    return render(request, 'books.html', {'publishers':publishers})
