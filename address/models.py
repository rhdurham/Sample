from django.db import models
from django.utils import timezone
#from django.db.models import F

# Create your models here.                                                                                                                                                         

class Profile(models.Model):
    title = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    
    def addresses(self):
        return self.addresses.all()
    
#    def __str__(self):
#        return '%s $s $s $s' % (self.title, self.first_name, self.middle_name, self.last_name)
    
class Address(models.Model):
    profile = models.ForeignKey(Profile,related_name='addresses', blank=True, null=True)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2);
    country = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)
    
#     def __str__(self):
#         return '%s %s %s' % (self.address_1, self.city, self.zipcode)
   
class MovieReview(models.Model):
    image_url = models.CharField(max_length=300)
    modification_date = models.DateTimeField(default=timezone.now)
    movie_description = models.TextField()
    movie_name = models.CharField(max_length=50)
    rating = models.CharField(max_length=10)
