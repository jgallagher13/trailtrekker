# Generated by Django 4.2.5 on 2023-10-06 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_alter_hiking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiking',
            name='date',
            field=models.DateField(verbose_name='hike date'),
        ),
    ]
