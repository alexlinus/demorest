from rest_framework import serializers
from cars.models import Car

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
