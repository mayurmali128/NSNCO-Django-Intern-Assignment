# from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from rest_framework import generics, filters
from .models import Work, Artist
from .serializers import UserSerializer, WorkSerializer, ArtistSerializer



class WorkList(generics.ListAPIView):
    serializer_class = WorkSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['artist__name']
    ordering_fields = ['link_type']

    def get_queryset(self):
        queryset = Work.objects.all()
        link_type = self.request.query_params.get('link_type')
        if link_type:
            queryset = queryset.filter(link_type=link_type)
        return queryset


class ArtistWorkList(generics.ListAPIView):
    serializer_class = WorkSerializer

    def get_queryset(self):
        artist_name = self.request.query_params.get('artist')
        if artist_name:
            artist = Artist.objects.get(name=artist_name)
            return artist.works.all()
        return Work.objects.all()


class RegisterUser(generics.CreateAPIView):
    serializer_class = UserSerializer

