# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Case(models.Model):
    id = models.AutoField(primary_key=True)
    confirmed_date = models.DateTimeField(blank=True, null=True)
    symptopmatic_at = models.DateTimeField(blank=True, null=True)
    recovered = models.BooleanField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    recovered_at = models.DateTimeField(blank=True, null=True)
    displayed_symptoms = models.BooleanField(blank=True, null=True)
    victim_fk = models.ForeignKey('Victims', models.DO_NOTHING, db_column='victim_fk', blank=True, null=True)
    case_type = models.CharField(max_length=250, blank=True, null=True)
    case_status = models.CharField(max_length=250, blank=True, null=True)
    country_of_origin = models.ForeignKey('Country', models.DO_NOTHING, db_column='country_of_origin', blank=True, null=True)
    status = models.ForeignKey('CaseStatus', models.DO_NOTHING, db_column='status', blank=True, null=True)
    infection_source = models.ForeignKey('InfectionSource', models.DO_NOTHING, db_column='infection_source', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'case'


class CaseStatus(models.Model):
    id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'case_status'

    def __str__(self):
        return self.status_name

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    countryname = models.CharField(max_length=250, blank=True, null=True)
    place_of_origin = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'

    def __str__(self):
        return self.countryname

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class InfectionSource(models.Model):
    id = models.AutoField(primary_key=True)
    source_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infection_source'
    
    def __str__(self):
        return self.source_name

class Victims(models.Model):
    id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    relationship = models.CharField(max_length=100, blank=True, null=True)
    citizen = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'victims'

    def __str__(self):
        return str(self.id)