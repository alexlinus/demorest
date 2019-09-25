from rest_framework import serializers
from cars.models import Car, Chat, Room, User


class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        #указываем модель, к которой будет привязан сериализатор. То же самое что и Modelform в django
        model = Car
        #Указываем поля, которые мы используем
        fields = '__all__'

class CarListSerializer(serializers.ModelSerializer):
    #Можно использовать hiddenfield, которое будет скрыто от редактирования.
    #По дефолту поставим туда, текущего авторизованного юзера. CurrentUserDefault()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Car
        fields = ['id', 'vin', 'user']
    #Делаем сериализатор, для того чтобы вывести все машины в базе данных
    #Причем мы будем выводить не все поля, а только часть.


#Чисто для примера, ннигде этот класс я в коде не использовал. Можно не искать его применение в коде проекта.
#Если нам не нужно использовать ModelSerializer, а допустим нужно просто проверить какие-то данные и отправить смс.
#То наследуемся от serializers.Serializer:

class ClassRandomNameIforgetHow(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    email = serializers.Serializer(label='Введите email', required=True)#можно много гибких настроек валидации задать.



#Если REST Является по сути валидацией, синхронизацией данных, и временным хранищем. А моделей у нас нет.
#То можно сделать serializer.Serializer и отправить их на внутреннюю часть системы. То есть Rest использовали как proxy,
#защищая внутреннюю разработку, от внешних пользователей. От воздействия из вне.


class UserSerializer(serializers.ModelSerializer):
    """ Сериализация пользователей """
    class Meta:
        model = User
        fields = ('id', 'username')


class RoomSerializer(serializers.ModelSerializer):
    """ Сериализация комнаты чата"""
    #Добавляем поле, creater теперь будет сериализоваться через UserSerializer
    #Т.к это foreignkey\manytomany, то мы сериализуем эти поля.invited и creater
    #
    creater = UserSerializer()
    #invited = UserSerializer(many=True)
    class Meta:
        model = Room
        fields = ('creater', 'invited', 'date')

#Получим тогда такой формат вывода json
#Т.к мы поле creater и invited сериализовали еще и внутри. То получилось многоуровневое.
#Если мы не будем сериализовать отдельно поле ссылающееся. То получится:
#        "invited": [
#            2
#        ],

#[
#    {
#        "creater": {
#            "id": 2,
#            "username": "admin"
#        },
#        "invited": [
#            {
#                "id": 2,
#                "username": "admin"
#            }
#        ],
#        "date": "2019-09-25T07:52:56.719598+03:00"
#    },

#Сериализитро используется для обработки информации с базы данных в json формат, и обратно.


class ChatSerializer(serializers.ModelSerializer):
    """ Сериализация чата """

    user = UserSerializer()
    class Meta:
        model = Chat
        fields = ('room', 'user', 'text', 'date')


#Здесь мы написали сериализатор для POST запроса. КОторый будет сериализовать текст сообщния и комнату.
#соотвесттеннно мы будем должны передать эти параметры в body
class ChatPostSerializer(serializers.ModelSerializer):
    """ Сериализация POST запроса """

    class Meta:
        model = Chat
        fields = ('text', 'room')