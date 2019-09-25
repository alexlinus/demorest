from django.shortcuts import render
from rest_framework import generics
from cars.serializers import CarDetailSerializer, CarListSerializer, RoomSerializer, ChatSerializer, ChatPostSerializer
# Create your views here.
from cars.models import Car, Chat, Room
from cars.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
#Если нам нужно чтобы смотрели только админы, IsAdminUser импортируем from rest_framework.permissions
from rest_framework.authentication import TokenAuthentication

from rest_framework.views import APIView
from rest_framework.response import Response

class CarCreateView(generics.CreateAPIView):
    #Т.к это CreateApiView будет доступе только POST метод
    serializer_class = CarDetailSerializer
    permission_classes = (IsAdminUser,)

class CarListView(generics.ListAPIView):
    #тк это ListApiView будут доступны только GET методы.
    serializer_class = CarListSerializer
    queryset = Car.objects.all()

    #Если нам нужно показывать список всех записей, только авторизованным пользователям
    permission_classes = (IsAuthenticated,)

class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    #RetrieveUpdateDestroyAPIView - позволяет обновлять, удалять, получать данные об одном объекте.
    #CarDetailSerializer -указываем уже созданный. Т.к нам нужны все поля, раз прсматриваем.
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    # Теперь к этой API запрещен доступ через web интерфейс. Только через Токен TokenAuthentication.
    # По базовой аутентификации мы не получим доступ. Только по токеновской аутентификации.
    # Мы можем указать через запятую, например Сессии или еще что. И тогда мы будем иметь доступ по сессии\кук например.
    authentication_classes = (TokenAuthentication,)
    # Даем права доступа к этой вьюхе. Редактировать может только тот человек, который эту вьюху сделал.
    # Стандартного функционала для этой возможности в джанго rest нет. Типа кто создал, тот и редактирует. Но другие типы permission есть.
    permission_classes = (IsOwnerOrReadOnly, )

class RoomView(APIView):
    """ Комнаты чата """

    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response({'data': serializer.data})

class DialogView(APIView):
    """ Диалог чата: сообщение """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        room = request.GET.get('room')
        chats = Chat.objects.filter(room=room)
        serializer = ChatSerializer(chats, many=True)
        return Response({'data': serializer.data})


    def post(self, request):
        #room = request.data.get('room')
        dialog = ChatPostSerializer(data=request.data)
        if dialog.is_valid():
            dialog.save(user=request.user)
            return Response({'status': 'Added successfull'})
        else:
            return Response({'status': 'error'})