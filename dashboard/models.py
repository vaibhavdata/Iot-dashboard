from email.policy import default
from operator import mod
from platform import release
from pyexpat import model
from django.db import models
from django.urls import reverse
import uuid
from shortuuid.django_fields import ShortUUIDField
# Create your models here.

class Device_Type(models.Model):
    device_name = models.CharField(max_length=50, unique=True)
    #slug = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=255, blank=True)
    device_image = models.ImageField(upload_to='photos/device_type', blank=True)

    class Meta:
        verbose_name = 'device_type'
        verbose_name_plural = 'device_types'
    def __str__(self):
        return self.device_name
class All_Type(models.Model):
    type = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.type
class Device(models.Model):
    LABEL_CHOICES = (
    ('Online', 'Online'),
    ('Offline', 'Offline'),
    ('Running','Running')
    )
    Release_Police = (
        ('defult','defult'),
        ('recommand','recommand')
    )
    name = models.CharField(max_length=200,blank=True)
    slug = models.CharField(max_length=200,blank=True)
    image = models.ImageField(upload_to='photos/device',blank=True)
    notes    = models.TextField(max_length=500, blank=True)
    status = models.CharField(choices=LABEL_CHOICES, max_length=50,null=True,blank=True)
    is_available    = models.BooleanField(default=True)
    device_type  = models.ForeignKey(Device_Type, on_delete=models.CASCADE ,blank=True, null=True)
    current_release =models.CharField(max_length=30)
    target_release = models.CharField(max_length=30)
    release_police= models.CharField(choices =Release_Police,max_length=50,null=True,blank=True)
    created_date    = models.DateTimeField(auto_now_add=True)
    
    all_type = models.ForeignKey(All_Type,on_delete=models.CASCADE,blank=True)
    uuid = ShortUUIDField(length=8,primary_key=True,default =uuid.uuid4(),editable = False)
    ip_address = models.CharField(max_length=200,blank=True)
    host_version =models.CharField(max_length=200,blank=True)
    last_login = models.DateTimeField(auto_now=True)
    def get_url(self):
        return reverse('device_detail', args=[self.slug])
    def __str__(self):
        return self.current_release
    
class Service_type(models.Model):
    service_name = models.CharField(max_length=200)
    def __str__(self):
        return self.service_name
class Service(models.Model):
    LABEL_CHOICES = (
        ('Online', 'Online'),
        ('Offline', 'Offline'),
        ('Running','Running')
    )
    name = models.CharField(max_length=20)
    service =models.ForeignKey(Service_type,on_delete=models.CASCADE)
    status = models.CharField(choices=LABEL_CHOICES, max_length=50,null=True,blank=True,default='Online')
    release = models.ForeignKey(Device,on_delete=models.CASCADE,blank=True)
    def __str__(self):
        return self.name

