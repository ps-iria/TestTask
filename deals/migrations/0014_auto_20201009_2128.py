# Generated by Django 3.1.2 on 2020-10-09 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0013_auto_20201009_2107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deals',
            name='gem',
        ),
        migrations.AddField(
            model_name='deals',
            name='gem',
            field=models.ManyToManyField(related_name='gems', to='deals.Gems'),
        ),
    ]
