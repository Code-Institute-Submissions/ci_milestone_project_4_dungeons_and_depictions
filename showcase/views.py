from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Commission, Category
from .forms import CommissionForm

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


@login_required
def add_commission(request):
    """ Add a commission to the showcase """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the showcase owner can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CommissionForm(request.POST, request.FILES)
        if form.is_valid():
            commission = form.save()
            messages.success(request, 'Successfully added commission!')
            return redirect(reverse('commission_detail', args=[commission.id]))
        else:
            messages.error(
                request, 'Failed to add commission. Please ensure the form is valid.')
    else:
        form = CommissionForm()

    template = 'commissions/add_commission.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_commission(request, commission_id):
    """ Edit a commission in the showcase """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the showcase owner can do that.')
        return redirect(reverse('home'))

    commission = get_object_or_404(Commission, pk=commission_id)
    if request.method == 'POST':
        form = CommissionForm(request.POST, request.FILES, instance=commission)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated commission!')
            return redirect(reverse('commission_detail', args=[commission.id]))
        else:
            messages.error(request, 'Failed to update commission. Please ensure the form is valid.')
    else:
        form = CommissionForm(instance=commission)
        messages.info(request, f'You are editing {commission.name}')

    template = 'commissions/edit_commission.html'
    context = {
        'form': form,
        'commission': commission,
    }

    return render(request, template, context)


@login_required
def delete_commission(request, commission_id):
    """ Delete a commission from the showcase """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the showcase owner can do that.')
        return redirect(reverse('home'))

    commission = get_object_or_404(Commission, pk=commission_id)
    commission.delete()
    messages.success(request, 'Commission deleted!')
    return redirect(reverse('commissions'))


@login_required
def request_commission(request):
    """ Allows users to request a commission """
    if request.method == 'POST':
        form = CommissionForm(request.POST, request.FILES)
        if form.is_valid():
            commission = form.save()
            messages.success(request, 'Commission request successfully added to cart!')
            return redirect(reverse('commission_detail', args=[commission.id]))
        else:
            messages.error(
                request, 'Failed to request a commission. Please ensure the form is valid.')
    else:
        form = CommissionForm()

    template = 'commissions/request_commission.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
