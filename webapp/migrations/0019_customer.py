# Generated by Django 5.1.4 on 2025-01-31 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0018_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]
