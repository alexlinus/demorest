from django.shortcuts import render
from rest_framework import generics
from cars.serializers import CarDetailSerializer, CarListSerializer
# Create your views here.
from cars.models import Car
from cars.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
#Если нам нужно чтобы смотрели только админы, IsAdminUser импортируем from rest_framework.permissions


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
    #Даем права доступа к этой вьюхе. Редактировать может только тот человек, который эту вьюху сделал.
    #Стандартного функционала для этой возможности в джанго rest нет. Типа кто создал, тот и редактирует. Но другие типы permission есть.
    permission_classes = (IsOwnerOrReadOnly, )