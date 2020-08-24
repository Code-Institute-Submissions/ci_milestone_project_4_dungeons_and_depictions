
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from showcase.models import Commission


def cart_contents(request):

    cart_items = []
    total = 0
    commission_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        commission = get_object_or_404(Commission, pk=item_id)
        total += item_data * commission.price
        commission_count += item_data
        cart_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'commission': commission,
        })

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'commission_count': commission_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
