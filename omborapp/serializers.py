from .models import *
from rest_framework import serializers

class OmborSer(serializers.ModelSerializer):
    class Meta:
        model = Ombor
        fields = "__all__"

class MahsulotSer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = "__all__"

class ClientSer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class StatsSer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = "__all__"