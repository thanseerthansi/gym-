# Generated by Django 3.2.6 on 2022-03-19 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetailsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_status', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Diet_PlanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_name', models.CharField(max_length=20)),
                ('d_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=20)),
                ('s_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_name', models.CharField(max_length=20)),
                ('e_type', models.ManyToManyField(to='coachapp.ExerciseTypeModel')),
            ],
        ),
    ]