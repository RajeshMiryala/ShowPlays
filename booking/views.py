from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
# Create your views here.
from booking.serializers import *
from django.db import transaction


def home(request):
    return HttpResponse("Hello World")


class GetPlayListViewSet(viewsets.GenericViewSet):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer

    def list(self, request):
        queryset = Play.objects.filter(is_active=1)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Play.objects.filter(screen__theater__city__name__icontains=pk, is_active=1)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddMovieViewSet(viewsets.GenericViewSet):
    queryset = Play.objects.all()
    serializer_class = AddUpdatePlaySerializer

    @transaction.atomic
    def create(self, request):
        data = request.data
        movie_data = data.pop('movie')
        screens = data.pop('screen')
        serializer = MovieSerializer(data=movie_data)
        if serializer.is_valid(raise_exception=True):
            movie_info = serializer.save()
        for scr in screens:
            Play.objects.filter(screen=scr['id']).update(is_active=0)
            screen_play = {'screen': scr['id'], 'movie': movie_info.id}
            play_serializer = self.serializer_class(data=screen_play)
            if play_serializer.is_valid(raise_exception=ValueError):
                play_serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)



