from django.contrib import admin
from .models import Car, Room, Chat
# Register your models here.
admin.site.register(Car)


class RoomAdmin(admin.ModelAdmin):
    list_display = ('creater', 'invited_user', 'date')

    def invited_user(self, obj):
        return "\n".join([user.username for user in obj.invited.all()])


admin.site.register(Room, RoomAdmin)


class ChatAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'text', 'date')



admin.site.register(Chat, ChatAdmin)