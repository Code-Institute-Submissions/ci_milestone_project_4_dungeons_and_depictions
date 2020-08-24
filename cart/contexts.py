from decimal import Decimal
from django.conf import settings


def cart_contents(request):

    cart_items = []
    total = 0
    commission_count = 0
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
