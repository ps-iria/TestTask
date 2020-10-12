# Generated by Django 3.1.2 on 2020-10-09 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0014_auto_20201009_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deals',
            name='gem',
        ),
        migrations.AddField(
            model_name='deals',
            name='gem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gems', to='deals.gems'),
        ),
    ]