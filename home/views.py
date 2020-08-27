from django.shortcuts import render

# Create your views here.


def index(request):
    """ This view returns the index page """
    return render(request, 'home/index.html')


def about(request):
    """ This view returns the about page """
    return render(request, 'home/about.html')
