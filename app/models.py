from django.db import models
from simple_history.models import HistoricalRecords
# from django_model_history_tracker.mixins import HistoryTrackerMixin
from django.utils import timezone

# Create your models here.

#class Person(HistoryTrackerMixin,models.Model):
class Person(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    contract_number = models.CharField(max_length=11)
    #history = HistoricalRecords()
    
    def save(self, *args, **kwargs):
        if not self.id:
            latest_id = Person.objects.latest('id').id if Person.objects.exists() else 1000
            self.id = latest_id + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.id} - {self.name}'

class Items(models.Model):
    LAPTOP = 'Laptop'
    HEADPHONE = 'Headphone'
    MOBILE = 'Mobile'
    SIM = 'Sim'

    CATEGORY_CHOICES = [
        (LAPTOP, 'Laptop'),
        (HEADPHONE, 'Headphone'),
        (MOBILE, 'Mobile'),
        (SIM, 'Sim'),
    ]

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES)
    handover_time = models.DateTimeField(blank=True,null=True)
    receive_time = models.DateTimeField(blank=True,null=True)
    user = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True,related_name='items_owned')
    handover_time_condition=models.TextField(blank=True,null=True)
    submitting_time_condition=models.TextField(blank=True,null=True)
    
    
    history = HistoricalRecords()
    def save(self, *args, **kwargs):
        if not self.id:
            latest_id = Items.objects.latest('id').id if Items.objects.exists() else 500
            self.id = latest_id + 1
        
        if self.user:
            self.handover_time = timezone.now()
            self.receive_time = None
        else:
            self.receive_time = timezone.now()
            self.handover_time=None

        super().save(*args, **kwargs)
