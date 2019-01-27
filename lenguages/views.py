from django.shortcuts import render
from rest_framework import viewsets
from .models import Languague
from .serializers import LanguagueSerializer

# Create your views here.
class LenguagueView(viewsets.ModelViewSet):
    queryset = Languague.objects.all()
    serializer_class = LanguagueSerializer