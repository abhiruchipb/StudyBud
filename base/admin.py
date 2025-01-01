from django.contrib import admin

# Register your models here.

#to view Room in the admin panel
from .models import Room, Topic, Message, User

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)