from random import choice
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Uylar(models.Model):
    CATEGORY_OF_HOME = {
        ("1", "Ijara"),
        ("2", "Sotuv")
    }

    CATEGORY_OF_CITY= {
        ("1","Toshkent Shahar"),
        ("2","Toshkent Viloyat"),
        ("3", "Farg'ona"),
        ("4", "Andijon"),
        ("5", "Namangan"),
        ("6", "Buxoro"),
        ("7", "Samarqand"),
        ("8", "Xorazm"),
        ("9", "Qashqadaryo"),
        ("10", "Surxandaryo"),
        ("11", "Navoiy"),
        ("12", "Qoraqalpog'iston")
    }

    XONALAR_SONI = {
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6")
    }

    BINO_QURILISHI = {
        ("1", "G'ishtli"),
        ("2", "Panel")
    }

    BOR_YOQ = {
        ("1", "Bor"),
        ("2", "Yo'q")
    }
    


    id = models.AutoField(primary_key=True)
    viloyat = models.CharField("Viloyat",default=1, choices=CATEGORY_OF_CITY, max_length=100)
    tuman = models.CharField("Tuman", max_length=250)
    orentir = models.CharField("Orentir", max_length=250)
    qurilish_yili = models.IntegerField("Qurilgan Yili")
    uy_turi = models.CharField("Tanlang",default=1, choices=CATEGORY_OF_HOME, max_length=100)
    xonalar_soni = models.CharField("Xonalar Soni", default=2, choices=XONALAR_SONI, max_length=1)
    xona_kattaligi = models.FloatField("Nechi Metr Kvadrat")
    jami_qavat = models.IntegerField("Jami Qavat")
    qavat = models.IntegerField("Qavat")
    bino_asosi = models.CharField("Bino Asosi", default=1, choices=BINO_QURILISHI, max_length=100)
    narxi = models.FloatField("Narxi -> $")

    Aftoturargox = models.CharField("Aftoturargox", default=1, choices=BOR_YOQ, max_length=100)    
    lift = models.CharField("Lift", default=2, choices=BOR_YOQ, max_length=100)
    qoriqlash = models.CharField("Qo'riqlash", default=2, choices=BOR_YOQ, max_length=100)
    video_kuzatuv = models.CharField("Video Kuzatuv", default=1, choices=BOR_YOQ, max_length=100)
    kanalizatsiya = models.CharField("Kanalizatsiya", default=1, choices=BOR_YOQ, max_length=100)
    bolalar_maydonchasi = models.CharField("Bolalar Maydonchasi", default=1, choices=BOR_YOQ, max_length=100)
    internet = models.CharField("Internet", default=1, choices=BOR_YOQ, max_length=5)
    qoshimcha_izoh = models.TextField("Izoh")
    rasm = models.ImageField("Uy Rasmi", upload_to ='images/')

    uy_egasi = models.CharField("Uy Egasi", max_length=50)
    telefon_raqami = models.CharField("Bog'lanish", max_length=14)
    
    author = models.ForeignKey(verbose_name="Muxbiri", default=1, to=User, on_delete=models.CASCADE, related_name="home_by_user")

    # for more info

    def __str__(self):
        return f"{self.id}, {self.viloyat}, {self.tuman}, {self.xonalar_soni}"

    class Meta:
        verbose_name = "Uylar"
        verbose_name_plural = "Uylar"

    