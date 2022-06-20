from rest_framework import generics
from .serializers import RestauListSerializer, RestauDetailSerializer
from .models import Restau


# Create your views here.

class RestauListAPIView(generics.ListAPIView):
    queryset = Restau.objects.all()
    serializer_class = RestauListSerializer


class RestauRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Restau.objects.all()
    serializer_class = RestauDetailSerializer


class RestauCreateAPIView(generics.CreateAPIView):
    queryset = Restau.objects.all()
    serializer_class = RestauDetailSerializer


class RestauRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    queryset = Restau.objects.all()
    serializer_class = RestauDetailSerializer


class RestauDestroyAPIView(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = Restau.objects.all()

