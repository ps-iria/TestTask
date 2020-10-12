# Generated by Django 3.1.2 on 2020-10-10 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0017_remove_gems_deals'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deals',
            options={'verbose_name': 'Deals'},
        ),
        migrations.RemoveField(
            model_name='deals',
            name='gem',
        ),
        migrations.AddField(
            model_name='deals',
            name='gem',
            field=models.ManyToManyField(null=True, related_name='gems', to='deals.Gems'),
        ),
    ]