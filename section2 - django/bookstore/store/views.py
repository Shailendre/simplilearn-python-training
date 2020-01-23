from django.shortcuts import render

# Create your views here.

# idea is to return the index template/ landing template
# index: name of the function is mentioned in url.py

# /store/index
# /store/
def index(request):
    return render(request, 'index.html')

# /store/v1
def v1(request):
    return render(request, 'v1.html')

# /store/v2
def v2(request):
    return render(request, 'v2.html')
