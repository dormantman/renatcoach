from rest_framework import serializers

from web.helpers import beauty_number
from web.models import Mail, Tariff


class TariffSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = Tariff
        fields = (
            'number',
            'title',
            'short',
            'warning_message',
            'warning_color',
            'price',
            'price_value',
            'price_label',
            'image',
            'button_name',
            'url'
        )
        read_only_fields = (
            'number',
            'title',
            'short',
            'warning_message',
            'warning_color',
            'price_value',
            'price_label',
            'image',
            'button_name',
            'url'
        )

    def get_price(self, model):
        return '<span>%s</span> %s' % (beauty_number(model.price_value), model.price_label)


class MailSerializer(serializers.ModelSerializer):
    tariff_data = serializers.SerializerMethodField()

    class Meta:
        model = Mail
        fields = (
            'name',
            'phone',
            'tariff',
            'tariff_data',
            'created'
        )
        read_only_fields = (
            'name',
            'phone',
            'tariff',
            'tariff_data',
            'created'
        )

    def get_tariff_data(self, model):
        qs = Tariff.objects.get(pk=model.tariff)
        return TariffSerializer(qs).data
