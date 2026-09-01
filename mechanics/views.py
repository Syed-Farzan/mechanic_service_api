from rest_framework import generics

from .models import Mechanic
from .serializers import MechanicSerializer


class MechanicListCreateView(generics.ListCreateAPIView):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSerializer


class MechanicDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSerializer
