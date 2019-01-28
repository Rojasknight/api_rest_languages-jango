from django.shortcuts import render
from rest_framework import viewsets
from .models import Languague, Programmer, Paradigm
from .serializers import LanguagueSerializer, ProgrammerSerializer, ParadigmSerializer

# Create your views here.
class LenguagueView(viewsets.ModelViewSet):
    queryset = Languague.objects.all()
    serializer_class = LanguagueSerializer

class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer

class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer