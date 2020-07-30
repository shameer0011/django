from django.db import models


# Create your models here.
class Address(models.Model):
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    image = models.ImageField(upload_to='image')

    def __str__(self):
       return self.name +","+ self.name

class Venue(models.Model):
    name=models.CharField('Venu Name', max_length=100)
    address=models.CharField(max_length=100)
    zip_code=models.CharField('Zip/Post code',max_length=100)
    phone=models.CharField('Contact Number',max_length=100)
    email_address=models.CharField('Email adress',max_length=19)

    

    def __str__(self):
       return self.name

class Event(models.Model):
    name=models.CharField('Event Name', max_length=100)
    event_date=models.CharField('Event date', max_length=100)
    venue=models.ForeignKey('Venue',on_delete=models.CASCADE)
    description=models.TextField(max_length=100)
    attendees=models.ManyToManyField(Address)

    def __str__(self):
        return self.name