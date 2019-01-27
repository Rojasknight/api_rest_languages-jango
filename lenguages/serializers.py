from rest_framework import serializers
from .models import Languague


class LanguagueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Languague
        fields = ('id', 'url', 'name', 'paradigm')
