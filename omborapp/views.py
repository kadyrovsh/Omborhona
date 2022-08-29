from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView


class OmborAPIView(APIView):
    def get(self, request):
        ombor = Ombor.objects.get(user=request.user)
        ser = OmborSer(ombor)
        return Response(ser.data)

class ClientlarAPIView(APIView):
    def get(self, request):
        clients = Client.objects.filter(user=request.user)
        ser = ClientSer(clients)
        return Response(ser.data)
    def post(self, request):
        malumot = request.data
        ser = ClientSer(data=malumot)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

class ClientAPIView(APIView):
    def put(self, request, pk):
        client = Client.objects.get(id=pk)
        ser = ClientSer(client)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_202_ACCEPTED)
        return Response(ser.data, status=status.HTTP_406_NOT_ACCEPTABLE)

class MahsulotlarAPIView(APIView):
    def get(self, request):
        mahsulotlar = Mahsulot.objects.filter(user=request.user)
        ser = MahsulotSer(mahsulotlar)
        return Response(ser.data)
    def post(self, request):
        malumot = request.data
        ser = MahsulotSer(data=malumot)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

class MahsulotAPIView(APIView):
    def put(self, request, pk):
        client = Mahsulot.objects.get(id=pk)
        ser = MahsulotSer(client)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_202_ACCEPTED)
        return Response(ser.data, status=status.HTTP_406_NOT_ACCEPTABLE)


class StatslarAPIView(APIView):
    def get(self, request):
        mahsulotlar = Stats.objects.filter(user=request.user)
        ser = StatsSer(mahsulotlar)
        return Response(ser.data)

    def post(self, request):
        malumot = request.data
        ser = StatsSer(data=malumot)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

class StatsAPIView(APIView):
    def put(self, request, pk):
        client = Stats.objects.get(id=pk)
        ser = StatsSer(client)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_202_ACCEPTED)
        return Response(ser.data, status=status.HTTP_406_NOT_ACCEPTABLE)
