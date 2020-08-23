from django.shortcuts import render
from .models import Commission

# Create your views here.


def all_commissions(request):
    """ A view to show all commissions, including sorting and search queries """

    commissions = Commission.objects.all()

    context = {
        'commissions': commissions,
    }

    return render(request, 'commissions/commissions.html', context)
