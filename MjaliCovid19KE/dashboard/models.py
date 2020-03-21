from django.db import models

# Create your models here.
class Case(models.Model):
    id = models.IntegerField(primary_key=True)
    confirmed_date = models.DateTimeField(blank=True, null=True)
    symptopmatic_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    recovered = models.BooleanField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    infection_source = models.CharField(max_length=250, blank=True, null=True)
    recovered_at = models.DateTimeField(blank=True, null=True)
    displayed_symptoms = models.BooleanField(blank=True, null=True)
    victim_fk = models.ForeignKey('victims.Victims', models.DO_NOTHING, db_column='victim_fk', blank=True, null=True)
    case_type = models.CharField(max_length=250, blank=True, null=True)
    case_status = models.CharField(max_length=250, blank=True, null=True)
    country_of_origin = models.ForeignKey('Country', models.DO_NOTHING, db_column='country_of_origin', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'case'


class Country(models.Model):
    id = models.IntegerField(primary_key=True)
    countryname = models.CharField(max_length=250, blank=True, null=True)
    place_of_origin = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'