from django.contrib.auth.models import User
from django.db import models

class Ombor(models.Model):
    ism = models.CharField(max_length=30)
    nom = models.CharField(max_length=40)
    tel = models.CharField(max_length=40)
    manzil = models.CharField(max_length=60)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.ism}, {self.nom}"

class Mahsulot(models.Model):
    nom = models.CharField(max_length=50)
    brend = models.CharField(max_length=50)
    k_narh = models.IntegerField()
    s_narh = models.IntegerField()
    miqdor = models.CharField(max_length=30)
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nom}, {self.brend}"

class Client(models.Model):
    dokon = models.CharField(max_length=50)
    ism = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    manzil = models.CharField(max_length=60)
    qarz = models.CharField(max_length=60)
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.ism}, {self.dokon}"

class Stats(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    sana = models.DateTimeField(auto_now_add=True)
    miqdor = models.IntegerField()
    umumiy = models.IntegerField()
    toladi = models.IntegerField()
    nasiya = models.IntegerField()
    ombor = models.ForeignKey(Ombor, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.client

