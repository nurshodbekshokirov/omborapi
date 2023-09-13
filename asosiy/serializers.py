from rest_framework import serializers
from .models import *
class MahsulotSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class OmborSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ombor
        fields = '__all__'