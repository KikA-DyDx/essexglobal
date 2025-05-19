from django.contrib import admin
from .models import Package, Sender, Receiver


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = (
        'tracking_number', 'status',
        'total_worth', 'total_worth_currency',
        'clearance_fee', 'clearance_fee_currency'
    )
    list_filter = ('status', 'total_worth_currency', 'clearance_fee_currency')
    search_fields = ('tracking_number', 'sender__name', 'receiver__name')
    ordering = ('-dispatch_date',)
    readonly_fields = ('tracking_number',)


admin.site.register(Sender)
admin.site.register(Receiver)
