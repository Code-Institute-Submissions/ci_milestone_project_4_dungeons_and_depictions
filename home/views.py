from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.contrib import messages
from .forms import ContactForm


def index(request):
    """ This view returns the index page """
    return render(request, 'home/index.html')


def about(request):
    """ This view returns the about page """
    return render(request, 'home/about.html')


def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            messages.success(request, 'Your email has been sent!')
            contact_name = request.POST.get(
                'contact_name', '')
            contact_email = request.POST.get(
                'contact_email', '')
            contact_order_number = request.POST.get(
                'contact_order_number', '')
            form_content = request.POST.get('content', '')

            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_order_number': contact_order_number,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" + '',
                ['youremail@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            email.send()
            return redirect('contact')
        else:
            messages.error(
                request, 'Failed to send email. Please ensure the form is valid.')

    return render(request, 'home/contact.html', {
        'form': form_class,
    })
