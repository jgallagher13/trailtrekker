# Generated by Django 4.2.5 on 2023-10-05 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_hiking_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hiking',
            options={'ordering': ['-date', 'created']},
        ),
    ]