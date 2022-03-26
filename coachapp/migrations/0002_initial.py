# Generated by Django 3.2.6 on 2022-03-19 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coachapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='customerdetailsmodel',
            name='customer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customerdetailsmodel',
            name='d_plan',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='coachapp.diet_planmodel'),
        ),
        migrations.AddField(
            model_name='customerdetailsmodel',
            name='schedule',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='coachapp.schedulemodel'),
        ),
    ]
