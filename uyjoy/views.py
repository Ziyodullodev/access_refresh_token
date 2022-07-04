from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Ijara
from .serializers import IjaraSerializer

# from django.contrib.auth.models import User
from users.models import MyUser
from users.serializers import UserSerializer

class IjaraAPIView(APIView):
    def get(self, request):
        data = Ijara.objects.all()
        ser = IjaraSerializer(data=data, many=True)
        if ser.is_valid():
            return Response(ser.data)
        return Response(ser.data)
        
    def post(self, request):
        data = request.data
        serializer = IjaraSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response({
            "ok":False
        })


class IjaraUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Ijara.objects.all()
    serializer_class = IjaraSerializer


def createuser(request):
    # User.objects.create(
    #     username = "ziyodullo",

    # )
    us = MyUser.objects.get(id=1)
    # print(us)
    ser = UserSerializer(us)
    if ser.is_valid():
        return Response(ser.data)
    return Response(ser.data)