from django.db import models
from django.db.models import Sum
    
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    quantity = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

    def calculate_total_sum(self):
        return Stock.objects.aggregate(sum=Sum('quantity'))['sum']

    def __str__(self):
	    return self.name