from django.db import models

# Create your models here.


class Podpischiki(models.Model):
    city = models.CharField(max_length=200, default='')
    name = models.CharField(max_length=200, default='')
    phone = models.CharField(max_length=200, default='')
    session_id = models.CharField(max_length=300, blank=True, default='')

    class Meta:
        verbose_name = "Заявки"
        verbose_name_plural = "заявки"

    def __str__(self):
        return self.name


