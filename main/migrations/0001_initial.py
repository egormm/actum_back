# Generated by Django 2.2 on 2019-04-28 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('ch_type', models.TextField(choices=[('дневные', 'дневные'), ('на спринт', 'на спринт')])),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(default='Хакатон Газпромович Актумов')),
                ('position', models.TextField(choices=[('программист', 'программист'), ('тестировщик', 'тестировщик'), ('аналитик', 'аналитик')], default='программист')),
                ('team', models.TextField(default='Лучшая команда в мире')),
                ('empl_rating', models.IntegerField(default=1, unique=True)),
                ('team_rating', models.IntegerField(default=1, unique=True)),
                ('tasks_per_day', models.IntegerField(default=1)),
                ('tasks_average', models.IntegerField(default=1)),
                ('points_per_day', models.IntegerField(default=1)),
                ('points_average', models.IntegerField(default=1)),
                ('team_tasks_per_day', models.IntegerField(default=1)),
                ('team_tasks_average', models.IntegerField(default=1)),
                ('team_points_per_day', models.IntegerField(default=1)),
                ('team_points_average', models.IntegerField(default=1)),
                ('mult', models.IntegerField(default=2)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('ev_type', models.TextField(choices=[('грамота', 'грамота'), ('письмо', 'письмо'), ('вызов на бой', 'вызов на бой'), ('информационная табличка', 'информационная табличка')], default='письмо')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('team_rating', models.IntegerField(default=1, unique=True)),
                ('team_tasks_per_day', models.IntegerField(default=1)),
                ('team_tasks_average', models.IntegerField(default=1)),
                ('team_points_per_day', models.IntegerField(default=1)),
                ('team_points_average', models.IntegerField(default=1)),
            ],
        ),
    ]
