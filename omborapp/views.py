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
        ombor = Ombor.objects.get(user=request.user)
        clients = Client.objects.filter(ombor=ombor)
        ser = ClientSer(clients)
        return Response(ser.data)
    def post(self, request):
        o =Ombor.objects.get(user=request.user)
        malumot = request.data
        ser = ClientSer(data=malumot)
        if ser.is_valid():
            ser.save(ombor=o)
            return Response(ser.data)
        return Response(ser.errors)

class ClientAPIView(APIView):
    def put(self, request, pk):
        o = Ombor.objects.get(user=request.user)
        client = Client.objects.get(id=pk)
        malumot = request.data
        ser = ClientSer(client, data=malumot)
        if ser.is_valid():
            ser.save(ombor=o)
            return Response(ser.data, status=status.HTTP_202_ACCEPTED)
        return Response(ser.data, status=status.HTTP_406_NOT_ACCEPTABLE)

class MahsulotlarAPIView(APIView):
    def get(self, request):
        ombor = Ombor.objects.get(user=request.user)
        mahsulotlar = Mahsulot.objects.filter(ombor=ombor)
        ser = MahsulotSer(mahsulotlar)
        return Response(ser.data)
    def post(self, request):
        o = Ombor.objects.get(user=request.user)
        malumot = request.data
        ser = MahsulotSer(data=malumot)
        if ser.is_valid():
            ser.save(ombor=o)
            return Response(ser.data)
        return Response(ser.errors)

class MahsulotAPIView(APIView):
    def put(self, request, pk):
        ombor = Ombor.objects.get(user=request.user)
        client = Mahsulot.objects.get(ombor=ombor)
        ser = MahsulotSer(client)
        if ser.is_valid():
            ser.save(ombor=ombor)
            return Response(ser.data, status=status.HTTP_202_ACCEPTED)
        return Response(ser.data, status=status.HTTP_406_NOT_ACCEPTABLE)


class StatslarAPIView(APIView):
    def get(self, request):
        ombor = Ombor.objects.get(user=request.user)
        mahsulotlar = Stats.objects.filter(ombor=ombor)
        ser = StatsSer(mahsulotlar)
        return Response(ser.data)

    def post(self, request):
        o = Ombor.objects.get(user=request.user)
        malumot = request.data
        ser = StatsSer(data=malumot)
        if ser.is_valid():
            ser.save(ombor=o)
            return Response(ser.data)
        return Response(ser.errors)

class StatsAPIView(APIView):
    def put(self, request, pk):
        ombor = Ombor.objects.get(user=request.user)
        stats = Stats.objects.get(id=pk)
        malumot = request.data
        ser = StatsSer(stats, data=malumot)
        if ser.is_valid() and stats.ombor == ombor:
            ser.save(ombor=ombor)
            return Response(ser.data, status=status.HTTP_202_ACCEPTED)
        return Response(ser.data, status=status.HTTP_406_NOT_ACCEPTABLE)
