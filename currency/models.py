from django.db import models

class CurrencyRate(models.Model):
    from_currency = models.CharField(max_length=3)
    to_currency = models.CharField(max_length=3)
    date = models.DateTimeField('rate date')
    rate = models.FloatField()