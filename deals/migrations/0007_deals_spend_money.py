# Generated by Django 3.1.2 on 2020-10-09 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0006_auto_20201009_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='deals',
            name='spend_money',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='deals.client'),
        ),
    ]
