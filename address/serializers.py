'''
Created on Oct 8, 2015

@author: rod
'''

from address.models import Profile, Address, MovieReview
from rest_framework import serializers

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'url','title','first_name', 'middle_name','last_name')
        
class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('id','url', 'profile','address_1','address_2', 'city', 'state', 'country', 'zipcode')
        
class MovieReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MovieReview
        fields = ('id', 'url', 'image_url', 'modification_date', 'movie_description', 'movie_name', 'rating', 'url')
        


