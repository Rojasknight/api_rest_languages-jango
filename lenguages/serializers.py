from rest_framework import serializers
from .models import Languague, Programmer, Paradigm


class LanguagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languague
        fields = ('id', 'url', 'name', 'paradigm')



class ParadigmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paradigm
        fields = ('id', 'url', 'name')


class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        fields = ('id', 'url', 'name', 'Languague')

