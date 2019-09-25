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


class Room(models.Model):
    """Model of chat room """
    creater = models.ForeignKey(User, verbose_name="Комната чата", on_delete=models.CASCADE)
    invited = models.ManyToManyField(User, verbose_name='Участники', related_name='invited_user')
    date = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Комната чата'
        verbose_name_plural = 'Комнаты чата'

    def __str__(self):
        return f'Комната номер: {self.id}'


class Chat(models.Model):
    """Model of chat"""
    room = models.ForeignKey(Room, verbose_name='Комната чата', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    text = models.TextField(max_length=100, verbose_name='Сообщение')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')

#https://www.youtube.com/watch?v=w0iXX5oyxQI
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


#Сериализитро используется для обработки информации с базы данных в json формат, и обратно.
