# Generated by Django 3.1.2 on 2020-10-09 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0009_auto_20201009_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deals',
            name='gem',
        ),
    ]