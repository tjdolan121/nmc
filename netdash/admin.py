from django.contrib import admin
from .models import ContactInfo, Service, Message, NetworkBoard, Unit

admin.site.register(ContactInfo)
admin.site.register(Service)
admin.site.register(Message)
admin.site.register(NetworkBoard)
admin.site.register(Unit)
