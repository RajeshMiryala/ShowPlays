from django.db import models

# Create your models here.


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, blank=False, null=False, unique=True)
    state = models.CharField(max_length=30, blank=True, null=False)

    class Meta:
        db_table = 'city'


class Theater(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, blank=False, null=False, unique=True)
    city = models.ForeignKey(City, models.DO_NOTHING, blank=False, null=False)

    class Meta:
        db_table = 'theater'
        unique_together = (('name', 'city'),)


class Screen(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, blank=False, null=False)
    theater = models.ForeignKey(Theater, models.DO_NOTHING, blank=False, null=False)

    class Meta:
        db_table = 'screen'
        unique_together = (('name', 'theater'),)


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, blank=False, null=False)
    description = models.CharField(max_length=500, blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False)
    language = models.CharField(max_length=30, blank=False, null=False)
    genere = models.CharField(max_length=30, blank=False, null=False)
    is_running = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'movie'
        unique_together = (('name', 'language'),)


class Play(models.Model):
    id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, models.DO_NOTHING, blank=False, null=False)
    screen = models.ForeignKey(Screen, models.DO_NOTHING, blank=False, null=False)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = 'play'