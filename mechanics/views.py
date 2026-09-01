from rest_framework import generics

from .models import Mechanic, ServiceRequest
from .serializers import MechanicSerializer, ServiceRequestSerializer


class MechanicListCreateView(generics.ListCreateAPIView):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSerializer


class MechanicDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSerializer


class ServiceRequestCreateView(generics.CreateAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
