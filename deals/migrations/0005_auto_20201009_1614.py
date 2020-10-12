# Generated by Django 3.1.2 on 2020-10-09 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0004_deals_gem'),
    ]

    operations = [
        migrations.AddField(
            model_name='gems',
            name='gem_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deals',
            name='gem',
            field=models.ManyToManyField(related_name='gems', to='deals.Gems'),
        ),
    ]