from django.core.exceptions import ValidationError
from django.db import models


class AboutStudent(models.Model):
    millati = models.CharField(max_length=40)
    fuqaroligi = models.CharField(max_length=40)
    malumoti = models.CharField(max_length=100)

    def __str__(self):
        return self.millati


class Student(models.Model):
    about = models.ForeignKey(AboutStudent,on_delete=models.CASCADE)
    username = models.CharField(max_length=155,default=' Ali')
    middlename = models.CharField(max_length=155,default='Alimov')
    born_date = models.DateTimeField()
    telefon = models.IntegerField(default=90-999-99-99)
    passport = models.CharField(max_length=21,default="pasport seriasi,raqami,jshshr raqami")

    def __str__(self):
        return self.username


class Languages(models.Model):
    chet_tili = models.CharField(max_length=255)
    sertifikat_turi = models.CharField(max_length=255, default='ielts,toefl')
    darajasi = models.FloatField(default=4.5)
    seretifikat = models.FileField(upload_to='sertifikat')

    def __str__(self):
        return self.chet_tili


class Otm_turi(models.Model):
    otm_nomi = models.CharField(max_length=100)

    def __str__(self):
        return self.otm_nomi


class Otm(models.Model):
    CHOICES = (
        ('kunduzgi', "kunduzgi talim"),
        ('kechki', "kechki talim"),
        ('sirtqi',"sirtqi")
    )
    CHOICE = (
        ('Magistratura', "Magistratura"),
        ('Bakalavir', "Bakalavir"),
    )

    otm_nomi = models.ForeignKey(Otm_turi, models.CASCADE)
    reyting_daftarchasi = models.FileField(upload_to="reyting_daftarchasi/")
    talim_turi= models.CharField(max_length=300, choices = CHOICE)
    talim_shali = models.CharField(max_length=300, choices = CHOICES)
    talim_bosqici = models.IntegerField(default=1)

    def clean(self):
        e = True
        for item in self.CHOICES:
            if self.talim_shali == item[0]:
                e = False
        if e:
            raise ValidationError("There is an error in the task type")


class Achievement(models.Model):
    sertificat_nomi = models.CharField(max_length=55)
    stipendiya = models.CharField(max_length=255, default="Beruniy,Navoiy stipendiyasi")
    yutuq1 = models.FileField(upload_to='achievments', default="Diplom, faxriy yorliq")
    yutuq2 = models.FileField(upload_to='achievments', default="Diplom, faxriy yorliq", blank=True)
    yutuq3 = models.FileField(upload_to='achievments', default="Diplom, faxriy yorliq", blank=True)
    yutuq4 = models.FileField(upload_to='achievments', default="Diplom, faxriy yorliq", blank=True)

    def __str__(self):
        return self.stipendiya


class ScientificAchievement(models.Model):
    risola = models.FileField(upload_to="ilmiy_yutuq")
    jurnal = models.FileField(upload_to="ilmiy_yutuq")
    conference = models.FileField(upload_to="ilmiy_yutuq")
    gazeta = models.FileField(upload_to="ilmiy_yutuq")

    def __str__(self):
        return self.risola


class Stipendiya(models.Model):
    stipendiya = models.CharField(max_length=55)


class TanlovMAlumotlari(models.Model):
    rektor_xati = models.FileField(upload_to="tanlov/")
    kengash_bayonnomasi = models.FileField(upload_to="tanlov/")
    i_r_hulosasi = models.FileField(upload_to="tanlov/")
    dekan_tavsiyasi = models.FileField(upload_to="tanlov/")
    stipendiya_nomzodligi = models.ForeignKey(Stipendiya, on_delete=models.CASCADE)




