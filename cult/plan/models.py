from django.db import models


# Create your models here.
class plan(models.Model):
    plan_name = models.CharField(max_length=50)
    cus_gmail_id = models.CharField(max_length=20)
    plan_duration = models.CharField(max_length=10)

    def __str__(self):
        return self.plan_name + '-' + self.cus_gmail_id + '-' + self.plan_duration
