from django.db import models
from django.contrib.auth.models import User

# Create your models here.
departments = [('Cardiologist', 'Cardiologist'),
               ('Dermatologists', 'Dermatologists'),
               ('Emergency Medicine Specialists',
                'Emergency Medicine Specialists'),
               ('Allergists/Immunologists', 'Allergists/Immunologists'),
               ('Anesthesiologists', 'Anesthesiologists'),
               ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')
               ]


class contact(models.Model):
    name = models.CharField(null=False, blank=False, max_length=122)
    email = models.CharField(null=False, blank=False, max_length=122)
    phone = models.CharField(null=False, blank=False, max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class Register(models.Model):
    first_name = models.CharField(max_length=122)
    last_name = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=122)
    username = models.CharField(max_length=122)
    password = models.CharField(max_length=18)

    def __str__(self):
        return self.username


class Cont(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Doctor(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.CharField(max_length=50)
    profile_pic = models.ImageField(
        upload_to='profile_pic/DoctorProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    department = models.CharField(
        max_length=50, choices=departments, default='Cardiologist')
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_id(self):
        return self.id

    def __str__(self):
        return "{} ({})".format(self.user.first_name, self.department)


class patientappointment(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=122)
    last_name = models.CharField(null=False, blank=False, max_length=122)
    phone = models.CharField(null=False, blank=False, max_length=12)
    date = models.DateTimeField(auto_now=True)
    age = models.CharField(null=False, blank=False, max_length=12)
    dieses = models.CharField(null=False, blank=False, max_length=18)
    address = models.CharField(null=False, blank=False, max_length=18)
    symptoms = models.CharField(null=False, blank=False, max_length=18)
    doctor_name = models.OneToOneField(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name




class Insurance(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    rate = models.CharField(max_length=12)
    desc = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
