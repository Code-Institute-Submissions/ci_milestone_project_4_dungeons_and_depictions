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
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                commissions = commissions.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            commissions = commissions.order_by(sortkey)

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

    current_sorting = f'{sort}_{direction}'

    context = {
        'commissions': commissions,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'commissions/commissions.html', context)


def commission_detail(request, commission_id):
    """ A view to show individual commission details """

    commission = get_object_or_404(Commission, pk=commission_id)

    context = {
        'commission': commission,
    }

    return render(request, 'commissions/commission_detail.html', context)
