from django.db import models


class MailQuerySet(models.QuerySet):
    """Extended manager for Mail model."""


class Mail(models.Model):
    text = models.CharField(max_length=1024, default='', blank=True)

    objects = MailQuerySet.as_manager()

    def __str__(self):
        return "Mail (%s)" % (self.text)

    class Meta:
        verbose_name = 'mail'
        verbose_name_plural = 'mails'
        ordering = ['id']
