# Generated by Django 2.2.9 on 2020-05-24 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20200524_2144'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mail',
            options={'ordering': ['id'], 'verbose_name': 'Письмо', 'verbose_name_plural': 'Письма'},
        ),
        migrations.AlterModelOptions(
            name='tariff',
            options={'ordering': ['number'], 'verbose_name': 'Тариф', 'verbose_name_plural': 'Тарифы'},
        ),
        migrations.AlterField(
            model_name='tariff',
            name='warning_message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
