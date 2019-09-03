from django.db import models

class phoneNumber(models.Model):
   phoneNumber_name = models.CharField('Имя контакта', max_length = 50)
   phoneNumber_number = models.CharField('Номер телефона', max_length = 20)	
	