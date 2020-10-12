# Generated by Django 3.1.2 on 2020-10-09 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0005_auto_20201009_1614'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deals',
            options={'ordering': ['-total']},
        ),
        migrations.RemoveField(
            model_name='client',
            name='gems',
        ),
        migrations.AlterField(
            model_name='client',
            name='spend_money',
            field=models.IntegerField(null=True),
        ),
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