from django.db import models


class Tracking(models.Model):
     name = models.CharField(max_length=100)
     tel = models.CharField(max_length=100)
     Tracking = models.CharField(max_length=100, null=True, blank=True)
     #other = models.TextChoices(null=False, blank=True)


     def __str__(self):
        return '{} - {} ({})'.format(self.name, self.tel, self.Tracking)

         