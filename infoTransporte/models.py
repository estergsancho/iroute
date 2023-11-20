from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=40)
    dni = models.CharField(primary_key=True, max_length=20)
    nombreUser = models.CharField(unique=True, max_length=20)

class Routestops(models.Model):
    id = models.IntegerField(primary_key=True)
    route = models.ForeignKey('Route', models.DO_NOTHING, blank=True, null=True)
    stop = models.ForeignKey('Stop', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RouteStops'


class Userstops(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    stop = models.ForeignKey('Stop', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserStops'


class Driver(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    email=models.CharField(max_length=200,blank=True,null=True)
    class Meta:
        managed = False
        db_table = 'driver'


class Route(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    start = models.CharField(max_length=100, blank=True, null=True)
    destination = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'route'


class Stop(models.Model):
    id = models.IntegerField(primary_key=True)
    latitud = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    name = models.CharField(max_length=200,blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'stop'


class StopArrivals(models.Model):
    id = models.OneToOneField(Stop, models.DO_NOTHING, db_column='id', primary_key=True)
    delay = models.IntegerField(blank=True, null=True)
    trafic = models.IntegerField(blank=True, null=True)
    weather = models.IntegerField(blank=True, null=True)
    accident = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stop_arrivals'


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    name_user = models.CharField(unique=True, max_length=100, blank=True, null=True)
    email=models.CharField(max_length=200)
    class Meta:
        managed = False
        db_table = 'user'


class Vechicle(models.Model):
    id = models.IntegerField(primary_key=True)
    capacity_left = models.IntegerField()
    type = models.CharField(max_length=100, blank=True, null=True)
    route = models.ForeignKey(Route, models.DO_NOTHING, blank=True, null=True)
    driver = models.ForeignKey(Driver, models.DO_NOTHING, blank=True, null=True)
    next_stop = models.ForeignKey(Stop, related_name='next_stop_set', on_delete=models.CASCADE)
    prev_stop = models.ForeignKey(Stop, related_name='prev_stop_set', on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'vechicle'
