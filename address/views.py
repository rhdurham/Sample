from django.shortcuts import render
from address.models import Profile, Address, MovieReview
from rest_framework import viewsets
from address.serializers import ProfileSerializer, AddressSerializer, MovieReviewSerializer

# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    
class MovieReviewViewSet(viewsets.ModelViewSet):
    queryset = MovieReview.objects.all()
    serializer_class = MovieReviewSerializer
