from django.db import models
from django.template.defaultfilters import slugify
from users.models import CustomUser


STATUS_CHOICES = (('FMC', 'FMC'), ('PMC', 'PMC'), ('NMC', 'NMC'), ('ASI', 'ASI'),)

PRIORITY_CHOICES = (('High', 'High'), ('Normal', 'Normal'), ('Low', 'Low'),)


class Unit(models.Model):
    title = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=50)
    favorites = models.ManyToManyField("self", blank=True)
    users = models.ManyToManyField(CustomUser)
    slug = models.SlugField(default='')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Unit, self).save(*args, **kwargs)


class ContactInfo(models.Model):
    poc = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    unit = models.OneToOneField(Unit, on_delete=models.CASCADE, related_name='contact_info')

    def __str__(self):
        return self.poc


class Message(models.Model):
    subject = models.CharField(max_length=50)
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=10, default='Normal')
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=1000)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='messages')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.subject


class NetworkBoard(models.Model):
    overall_status = models.CharField(choices=STATUS_CHOICES, max_length=3)
    updated_at = models.DateTimeField(auto_now=True)
    unit = models.OneToOneField(Unit, on_delete=models.CASCADE, related_name='network_board')

    def __str__(self):
        return "{}: {}".format(self.unit, self.overall_status)


class Service(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)
    more_info = models.TextField(max_length=500, blank=True)
    network_board = models.ForeignKey(NetworkBoard, on_delete=models.CASCADE, related_name='services')

    def __str__(self):
        return self.name
