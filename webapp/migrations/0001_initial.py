# Generated by Django 5.1.4 on 2025-01-13 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('uname', models.CharField(max_length=50)),
                ('upassword', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]
