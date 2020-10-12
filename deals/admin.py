from django.contrib import admin

# Register your models here.
from deals.models import Deals


class DealsAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'username',
        'item',
        'total',
        'quantity',
        'date',
    )
    list_filter = (
        'date',
    )
    search_fields = (
        'pk',
    )
admin.site.register(Deals, DealsAdmin)