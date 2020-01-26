from django.shortcuts import render
from .models import Book
# Create your views here.

# idea is to return the index template/ landing template
# index: name of the function is mentioned in url.py

# /store/index
# /store/
def index(request):
    # orm query
    # number of books
    count = Book.objects.all().count() # books as an objects get all, get the count
    # need to create a context map, so that the `count`, can be used in template
    return render(request, 'index.html',  {'count' : count})

# /store/v1
def v1(request):
    return render(request, 'v1.html')

# /store/v2
def v2(request):
    return render(request, 'v2.html')
