from django.db import models
class person(models.model):
    gender_choices=((u'M',u'male'),(u'F',u'Female'),)
    fname=models.CharField(max_length=30)
    sname=models.CharField(max_length=30)
    gender=models.CharField(max_length=2,choices=gender_choices)
