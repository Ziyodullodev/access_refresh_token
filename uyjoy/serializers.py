from rest_framework.serializers import ModelSerializer
from .models import Ijara

class IjaraSerializer(ModelSerializer):
    class Meta:
        model = Ijara
        fields = ['manzil', 'lokatsiya','malumot', 'ism','telefon','email', 'ijaranarxi','user', "rasm"]
