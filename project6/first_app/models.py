from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 20)
    father_name = models.CharField(max_length=20)
    address = models.TextField()
    reg_no = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    email_field = models.EmailField()
    positive_big_integer_field = models.PositiveBigIntegerField()