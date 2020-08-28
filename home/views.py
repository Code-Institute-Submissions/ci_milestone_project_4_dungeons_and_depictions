from django.shortcuts import render
from .forms import ContactForm


def index(request):
    """ This view returns the index page """
    return render(request, 'home/index.html')


def about(request):
    """ This view returns the about page """
    return render(request, 'home/about.html')


def contact(request):
    form_class = ContactForm

    return render(request, 'home/contact.html', {
        'form': form_class,
    })
