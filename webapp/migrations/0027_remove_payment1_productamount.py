# Generated by Django 5.1.4 on 2025-02-03 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0026_payment1_productamount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment1',
            name='productamount',
        ),
    ]
