from django.db import models


class Student(models.Model):
    uuid = models.CharField(max_length=36, unique=True, primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    ethnicity = models.CharField(max_length=100)
    uni = models.CharField(max_length=100)
    grad_date = models.CharField(max_length=100)

    points = models.IntegerField(default=0)

