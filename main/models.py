from django.db import models


class Talaba(models.Model):
    ism = models.CharField(max_length=100)
    guruh = models.CharField(max_length=50)
    kurs = models.IntegerField()
    kitob_soni = models.IntegerField()

    class Meta:
        verbose_name_plural = "Talabalar"

    def __str__(self):
        return self.ism


class Muallif(models.Model):
    ism = models.CharField(max_length=100)
    jins_choices = [
        ('A', 'Erkak'),
        ('F', 'Ayol'),
    ]
    jins = models.CharField(max_length=1, choices=jins_choices)
    tugilgan_sana = models.DateField()
    kitob_soni = models.IntegerField()
    tirik = models.BooleanField()
    yosh = models.DateField()


    class Meta:
        verbose_name_plural = 'Mualliflar'

    def __str__(self):
        return self.ism


class Kitob(models.Model):
    nom = models.CharField(max_length=200)
    janr_choices = [
        ('Badiiy', 'Badiiy'),
        ('Ilmiy', 'Ilmiy'),
    ]
    janr = models.CharField(max_length=10, choices=janr_choices)
    sahifa = models.IntegerField()
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Kitoblar'

    def __str__(self):
        return self.nom

class Admin(models.Model):
    ism = models.CharField(max_length=100)
    ish_vaqti = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Adminlar'

    def __str__(self):
        return self.ism


class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    olingan_sana = models.DateField()
    qaytarish_sana = models.DateField()
    kitob_obj = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Recordlar'

    def __str__(self):
        return f'{self.talaba} - {self.kitob}'


class Profil(models.Model):
    ism = models.CharField(max_length=100)
    yosh = models.IntegerField()
    sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ism

class Kurs(models.Model):
    nom = models.CharField(max_length=100)
    daraja = models.CharField(max_length=50)
    ustoz = models.CharField(max_length=100)
    narx = models.DecimalField(max_digits=10, decimal_places=2)
    chegirma = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.nom

class Izoh(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    matn = models.TextField()
    sana = models.DateTimeField(auto_now_add=True)
    baho = models.IntegerField()

    def __str__(self):
        return self.profil

class Tanlangan(models.Model):
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)

    def __str__(self):
        return self.kurs

class Xarid(models.Model):
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    sana = models.DateTimeField(auto_now_add=True)
    holat = models.CharField(max_length=100)

    def __str__(self):
        return self.kurs

class Student(models.Model):
    ful_name = models.CharField(max_length=255)
    course = models.PositiveSmallIntegerField(default=1)
    birthdate = models.DateField(blank=True, null=True)
    gpa = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='student/')

    def __str__(self):
        return self.ful_name

class Universitet(models.Model):
    nom = models.CharField(max_length=255)
    ochilgan_sana = models.DateField()
    talaba_soni = models.PositiveIntegerField()
    sayt = models.URLField()
    yillik = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nom

class Yonalish(models.Model):
    nom = models.CharField(max_length=100)
    aktiv = models.BooleanField(default=True)
    main_yonalish = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class Fan(models.Model):
    nom = models.CharField(max_length=100)
    asosiy = models.BooleanField(default=False)
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Ustoz(models.Model):
    JINS_CHOICES = [
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol'),
    ]
    DARAJA_CHOICES = [
        ('Bakalavr', 'Bakalavr'),
        ('Magistr', 'Magistr'),
    ]

    ism = models.CharField(max_length=100)
    yosh = models.IntegerField()
    jins = models.CharField(max_length=10, choices=JINS_CHOICES)
    daraja = models.CharField(max_length=10, choices=DARAJA_CHOICES)
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE)
    main_ustoz = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Ustoz'
        verbose_name_plural = 'Ustozlar'

    def __str__(self):
        return self.ism




