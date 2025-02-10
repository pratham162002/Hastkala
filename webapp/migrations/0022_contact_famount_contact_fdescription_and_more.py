# Generated by Django 5.1.4 on 2025-02-02 17:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0021_payment1_address_payment1_dob_payment1_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='famount',
            field=models.IntegerField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='fdescription',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment1',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.product'),
        ),
    ]
