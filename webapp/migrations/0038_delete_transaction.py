# Generated by Django 5.1.4 on 2025-02-04 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0037_cartitem_total_amount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
