# Generated by Django 5.1.4 on 2025-02-17 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0046_alter_comment_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='message',
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
