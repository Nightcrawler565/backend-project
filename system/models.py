from django.db import models


class Customers(models.Model):
    customer_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone_number = models.BigIntegerField()
    monthly_salary = models.IntegerField()
    approved_limit = models.IntegerField()
    current_debt = models.IntegerField(default=0)

    def __str__(self):
        return self.last_name

class LoanData(models.Model):
    customer_id=models.IntegerField()
    loan_id=models.IntegerField()
    loan_amount=models.IntegerField()
    tenure=models.IntegerField()
    interest_rate=models.FloatField()
    emi=models.IntegerField()
    emi_on_time=models.IntegerField(default=0)
    start_date=models.DateField()
    end_date=models.DateField()

    def __int__(self):
        return self.customer_id


# Create your models here.
