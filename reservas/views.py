from rest_framework import viewsets
from .models import Usuario, Cita
from .serializers import UsuarioSerializer, CitaSerializer

class UsuarioViewSet(viewsets.ModelViewSet):   # 👈 ESTE debe ser ModelViewSet
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer
