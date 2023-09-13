
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import *
from .models import *
from .serializers import *

class StatsViewset(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Stats.objects.all()
    serializer_class = StatsSerializers

# Create your views here.
