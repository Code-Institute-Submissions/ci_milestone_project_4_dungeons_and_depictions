from django.shortcuts import render, get_object_or_404
from .models import Commission

# Create your views here.


def all_commissions(request):
    """ A view to show all commissions, including sorting and search queries """

    commissions = Commission.objects.all()

    context = {
        'commissions': commissions,
    }

    return render(request, 'commissions/commissions.html', context)


def commission_detail(request, commission_id):
    """ A view to show individual commission details """

    commission = get_object_or_404(Commission, pk=commission_id)

    context = {
        'commission': commission,
    }

    return render(request, 'commissions/commission_detail.html', context)
