from django.db import models

class Victims(models.Model):
    id = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    relationship = models.CharField(max_length=100, blank=True, null=True)
    citizen = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'victims'
