from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    birth_date = models.DateField()
    joining_date = models.DateField()
    
    def __str__(self):
        return self.name


class Events(models.Model):
    EVENT_CHOICES = (
        ('birt_hday', 'Birthday'),
        ('work_anniversary', 'Work Anniversary'),
    )

    event_type = models.CharField(max_length=20, choices=EVENT_CHOICES)
    event_date = models.DateField()

    def __str__(self):
        return f"{self.get_event_type_display()} - {self.event_date}"

class EmailTemplate(models.Model):
    EVENT_CHOICES = (
        ('birthday', 'Birthday'),
        ('work_anniversary', 'Work Anniversary'),
    )

    event_type = models.CharField(max_length=20, choices=EVENT_CHOICES, unique=True)
    subject = models.CharField(max_length=255)
    template_name = models.CharField(max_length=255)

    def __str__(self):
        return self.event_type


class EventType(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Event(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    event_date = models.DateField()


