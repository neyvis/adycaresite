from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Class(models.Model):
    name = models.CharField(max_length=200)
    overview = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    info = models.CharField(max_length=2000)
    menu_overview = models.CharField(max_length=200)
    menu_description = models.CharField(max_length=2000)

    def __str__(self):
        return self.name

class Educator(models.Model):
    class_name = models.ForeignKey(Class, null=True)
    name = models.CharField(max_length=200)
    picture = models.ImageField(blank=True, null=True)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.name

class Milestone(models.Model):
    class_name = models.ForeignKey(Class, null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name