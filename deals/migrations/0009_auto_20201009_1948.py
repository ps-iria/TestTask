# Generated by Django 3.1.2 on 2020-10-09 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0008_auto_20201009_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deals',
            name='gem',
            field=models.ManyToManyField(to='deals.Gems'),
        ),
    ]
