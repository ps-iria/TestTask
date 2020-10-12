# Generated by Django 3.1.2 on 2020-10-08 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('spend_money', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('item', models.CharField(max_length=50)),
                ('total', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
