from django.db import models


class MailQuerySet(models.QuerySet):
    """Extended manager for Mail model."""


class Mail(models.Model):
    name = models.CharField(max_length=1024, default='Анонимный пользователь', blank=True)
    phone = models.CharField(max_length=1024, default='88008880088', blank=True)
    tariff = models.IntegerField(default=-1, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    objects = MailQuerySet.as_manager()

    def __str__(self):
        return "Mail (%s | %s | %s)" % (self.name, self.phone, self.tariff)

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'
        ordering = ['id']


class TariffQuerySet(models.QuerySet):
    """Extended manager for Tariff model."""


class Tariff(models.Model):
    number = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=1024, default='Новый тариф', blank=True)
    short = models.CharField(max_length=1024, default='Тариф', blank=True)
    warning_message = models.TextField(null=True, blank=True)
    warning_color = models.CharField(max_length=1024, null=True, blank=True)
    price_value = models.IntegerField(default=0, null=True, blank=True)
    price_label = models.CharField(max_length=1024, default='<span>0</span> рублей', blank=True)
    image = models.CharField(max_length=1024, null=True, blank=True)
    button_name = models.CharField(max_length=1024, default='Договориться', blank=True)
    url = models.CharField(max_length=1024, default='#mail', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    objects = MailQuerySet.as_manager()

    def __str__(self):
        return "Tariff (%s | %s)" % (self.title, self.price_label)

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'
        ordering = ['number']
