from django.db import models


class Team(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=False, null=False)
    rating = models.IntegerField(blank=False, default=1, unique=True)
    tasks_per_day = models.IntegerField(default=1)
    tasks_average = models.IntegerField(default=1)
    points_per_day = models.IntegerField(default=1)
    points_average = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(default='Хакатон Газпромович Актумов')
    position = models.TextField(choices=[('программист', 'программист'),
                                         ('тестировщик', 'тестировщик'),
                                         ('аналитик', 'аналитик')], default='программист')
    team = models.TextField(default='Лучшая команда в мире')
    rating = models.IntegerField(blank=False, default=1, unique=True)
    team_rating = models.IntegerField(blank=False, default=1)
    tasks_per_day = models.IntegerField(default=1)
    tasks_average = models.IntegerField(default=1)
    points_per_day = models.IntegerField(default=1)
    points_average = models.IntegerField(default=1)
    team_tasks_per_day = models.IntegerField(default=1)
    team_tasks_average = models.IntegerField(default=1)
    team_points_per_day = models.IntegerField(default=1)
    team_points_average = models.IntegerField(default=1)
    mult = models.IntegerField(default=2)

    def __str__(self):
        return self.name


class Events(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.TextField()
    ev_type = models.TextField(choices=[('грамота', 'грамота'),
                                        ('письмо', 'письмо'),
                                        ('вызов на бой', 'вызов на бой'),
                                        ('информационная табличка', 'информационная табличка')], default='письмо')

    def __str__(self):
        return self.description[:15]


class Challenge(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.TextField()
    ch_type = models.TextField(choices=[('дневные', 'дневные'),
                                        ('на спринт', 'на спринт')])

    def __str__(self):
        return self.description[:15]
