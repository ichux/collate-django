from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)


class Book(models.Model):
    title = models.CharField(null=False, blank=False, max_length=180)
    author = models.ForeignKey("Author", on_delete=models.RESTRICT)
