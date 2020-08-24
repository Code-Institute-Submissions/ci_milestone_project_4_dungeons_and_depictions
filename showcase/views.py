from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Commission, Category

# Create your views here.


def all_commissions(request):
    """ A view to show all commissions, including sorting and search queries """

    commissions = Commission.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            commissions = commissions.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('commissions'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            commissions = commissions.filter(queries)

    context = {
        'commissions': commissions,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'commissions/commissions.html', context)


def commission_detail(request, commission_id):
    """ A view to show individual commission details """

    commission = get_object_or_404(Commission, pk=commission_id)

    context = {
        'commission': commission,
    }

    return render(request, 'commissions/commission_detail.html', context)
