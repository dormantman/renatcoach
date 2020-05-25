from django.core import mail

from web.models import Mail, Tariff
from web.serializers import MailSerializer, TariffSerializer


def get_tariffs():
    tariffs = Tariff.objects.all()
    data = TariffSerializer(tariffs, many=True).data
    return [tariff for tariff in sorted(data, key=lambda t: t['number'])]


def get_emails():
    emails = Mail.objects.all()
    data = MailSerializer(emails, many=True).data
    return [tariff for tariff in sorted(data, key=lambda t: t['created'])]


def send_email(*args, **kwargs):
    additional = kwargs.pop('additional')

    email = mail.EmailMessage(*args, **kwargs)
    email.content_subtype = "html"
    status = email.send()

    if status:
        print('Save new letter...')
        email_model = Mail(
            name=additional['name'],
            phone=additional['phone'],
            tariff=additional['tariff']['number'],
        )
        email_model.save()

    return status
