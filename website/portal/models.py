from django.db import models

# Create your models here.
class College(models.Model):
    institute = models.CharField(max_length=200, default='NaN')
    program_name = models.CharField(max_length=200, default='NaN')
    quota = models.CharField(max_length=50, default='NaN')
    seat_type = models.CharField(max_length=50, default='NaN')
    gender = models.CharField(max_length=50, default='NaN')
    opening_rank = models.CharField(max_length=50, default='NaN')
    closing_rank = models.CharField(max_length=50, default='NaN')
    year = models.CharField(max_length=50, default='NaN')
    round = models.CharField(max_length=50, default='NaN')

