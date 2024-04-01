from .models import Drmtm
from rest_framework import viewsets, permissions
from .serializers import DrmtmSerializer

# Create your views here.
class DrmtmViewSet(viewsets.ModelViewSet):
    queryset=Drmtm.objects.all()
    serializer_class=DrmtmSerializer
    permission_classes=[permissions.AllowAny]