# Generated by Django 3.2.6 on 2022-03-21 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managerapp', '0001_initial'),
        ('loginapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='subscriptionplan_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='managerapp.planmodel'),
        ),
    ]