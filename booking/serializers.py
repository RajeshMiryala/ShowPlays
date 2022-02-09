from rest_framework import serializers
from booking.models import *


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('name', 'description', 'duration', 'language')


class ScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('name')


class PlaySerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    screen = serializers.CharField(read_only=True, source="screen.name")
    screen_id = serializers.CharField(read_only=True, source="screen.id")
    theater = serializers.CharField(read_only=True, source="screen.theater.name")
    city = serializers.CharField(read_only=True, source="screen.theater.city.name")

    class Meta:
        model = Play
        fields = '__all__'


class AddUpdatePlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = '__all__'