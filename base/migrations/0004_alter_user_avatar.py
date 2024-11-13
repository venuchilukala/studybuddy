# Generated by Django 5.1.3 on 2024-11-13 17:29

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=django_resized.forms.ResizedImageField(crop=None, default='avatar.svg', force_format=None, keep_meta=True, null=True, quality=85, scale=None, size=[600, 600], upload_to=''),
        ),
    ]
