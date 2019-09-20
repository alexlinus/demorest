from rest_framework import permissions

#Мы этот файл permissions создали сами

#Данный сниппет, есть в гугле и его используют практически все
#То есть мы использовали
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #Проверяет является ли этот метод безопасным SAFe METHODS это константа и вкллючаю в себя GET, HEAD, Options
        if request.method in permissions.SAFE_METHODS:
            return True
        #Проверяем является совпадает юзер объекта нашего с юзером запроса. С юзером, который авторизован.
        return obj.user == request.user