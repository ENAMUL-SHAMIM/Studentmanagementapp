from django.db import models

# Create your models here.
class Student(models.Model):
    reg_number = models.CharField(max_length=20)
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=30)
    age = models.IntegerField()

    class Meta:
        db_table = "student"