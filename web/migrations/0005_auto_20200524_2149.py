# Generated by Django 2.2.9 on 2020-05-24 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20200524_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='warning_color',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
