from django.db import models
from django.contrib.auth import get_user_model

#Т.к в теории модель юзера может быть переопределена. То наследоваться от стандартной модели User джанги нельзя.
#Поэтому мы импортируем get_user_model и переопределям User. ТО есть User моодель не джанговская, а теперь своя, отдельная.
# Получается User = from django.contrib.auth import User
#Возникнут вопросы, https://www.youtube.com/watch?v=C6S3dMt1s_M 52:06
User = get_user_model()
# Create your models here.

class Car(models.Model):
    vin = models.CharField(verbose_name='Vin', db_index=True, unique=True, max_length=64)
    color = models.CharField(verbose_name='Color', max_length=64)
    brand = models.CharField(verbose_name='Brand', max_length=64)
    CAR_TYPES = (
        (1, 'Седан'),
        (2, 'Хэчбек'),
        (3, 'Универсал'),
        (4, 'Купе'),
    )
    car_type = models.IntegerField(verbose_name='Car_Type', choices=CAR_TYPES)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)