from django.contrib import admin
from django.utils.safestring import mark_safe

from web.helpers import beauty_number
from web.models import Mail, Tariff


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    model = Mail
    list_display = ('name', 'phone', 'tariff', 'created',)
    list_filter = ('name', 'phone', 'tariff', 'created',)
    fieldsets = (
        (None, {'fields': ('name', 'phone', 'tariff', 'created')}),
    )
    readonly_fields = ('id', 'created',)
    search_fields = ('id',)
    ordering = ('created',)


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    model = Tariff
    list_display = (
        'number', 'title', 'created', 'get_price',
    )
    list_filter = (
        'number', 'title', 'price_value', 'price_label',
    )
    fieldsets = (
        (None, {
            'fields': (
                'number', 'title', 'short', 'warning_message', 'warning_color', 'price_value', 'price_label', 'image',
                'button_name', 'url')
        }),
    )
    readonly_fields = ('number',)
    search_fields = ('title',)
    ordering = ('created', 'number', 'title',)

    def get_price(self, model):
        return mark_safe(
            '<span>%s</span> %s' % (
                beauty_number(model.price_value),
                model.price_label
            )
        )
