from django.db import models


class DealFile(models.Model):
    deal = models.FileField(upload_to='deal/')


class Deals(models.Model):
    username = models.CharField(max_length=50)
    item = models.CharField(max_length=50)
    total = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        verbose_name = ('Deals')

    def get_username(self):
        return self.username





