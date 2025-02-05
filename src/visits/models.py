from django.db import models

# Create your models here.
class PageVisit(models.Model):
    # db table
    # id --> primary key --> autofield --> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    path = models.CharField(blank=True, null=True,max_length=255)
    #count = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)