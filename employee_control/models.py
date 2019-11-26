from django.db import models
from django.contrib.auth.models import User
import datetime 

# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete='CASCADE')

    # additional
    birth_date = models.DateField(blank=True, null=True)
    CPF = models.CharField(max_length=14, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(max_length=11, blank=True, null=True)
    role = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    id_departament = models.IntegerField(blank=True, null=True)
    id_supervisor = models.IntegerField(blank=True, null=True)
    profile_img = models.ImageField(upload_to='profile_pics',blank=True, null=True)

    @property
    def age(self):
        born = self.birth_date
        today = datetime.date.today()
        try: # Verifica se a data atual é 29 de Fevereiro e não é ano bissexto
            birthday = born.replace(year=today.year)
        except ValueError:
            birthday = born.replace(year=today.year, day=born.day - 1)

        if birthday > today:
            return (today.year - born.year - 1)
        else:
            return today.year - born.year
    
    def __str__(self):
        return self.user.username
