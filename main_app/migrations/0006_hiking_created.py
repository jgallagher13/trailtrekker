# Generated by Django 4.2.5 on 2023-10-05 17:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_trail_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='hiking',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
