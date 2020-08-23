from django.contrib import admin
from .models import Commission, Category

# Register your models here.


class CommissionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'category',
        'price',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Commission, CommissionAdmin)
admin.site.register(Category, CategoryAdmin)
