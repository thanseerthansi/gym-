# Generated by Django 3.2.6 on 2022-03-19 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(default='', max_length=20, unique=True)),
                ('p_price', models.FloatField(default=0.0)),
                ('discription', models.TextField()),
            ],
        ),
    ]