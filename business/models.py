from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)


class Book(models.Model):
    title = models.CharField(null=False, blank=False, max_length=180)
    author = models.ForeignKey("Author", on_delete=models.RESTRICT)


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class AccessLog(models.Model):
    ip = models.GenericIPAddressField(blank=True, null=True)
    ts = models.DateTimeField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "access_log"


class Cities(models.Model):
    _id = models.BigIntegerField(blank=True, null=True)
    pos = models.TextField(blank=True, null=True)  # This field type is a guess.
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "cities"


class Factbook(models.Model):
    year = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    shares = models.BigIntegerField(blank=True, null=True)
    trades = models.BigIntegerField(blank=True, null=True)
    dollars = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "factbook"


class Hashtag(models.Model):
    id = models.BigIntegerField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    uname = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)  # This field type is a guess.
    hashtags = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = "hashtag"


class Hello(models.Model):
    language = models.TextField(blank=True, null=True)
    hello = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "hello"


class Pubnames(models.Model):
    _id = models.BigIntegerField(blank=True, null=True)
    pos = models.TextField(blank=True, null=True)  # This field type is a guess.
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "pubnames"


class Rate(models.Model):
    currency = models.TextField(blank=True, null=True)
    validity = models.TextField(blank=True, null=True)  # This field type is a guess.
    value = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "rate"


class Rates(models.Model):
    currency = models.TextField(blank=True, null=True)
    validity = models.TextField(blank=True, null=True)  # This field type is a guess.
    rate = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "rates"


class Tweet(models.Model):
    id = models.BigIntegerField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    hour = models.TimeField(blank=True, null=True)
    uname = models.TextField(blank=True, null=True)
    nickname = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    favs = models.BigIntegerField(blank=True, null=True)
    rts = models.BigIntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    place = models.TextField(blank=True, null=True)
    picture = models.TextField(blank=True, null=True)
    followers = models.BigIntegerField(blank=True, null=True)
    following = models.BigIntegerField(blank=True, null=True)
    listed = models.BigIntegerField(blank=True, null=True)
    lang = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tweet"
