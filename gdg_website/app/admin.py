from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(Event)
admin.site.register(Team)
admin.site.register(Project)
admin.site.register(Subscriber)
admin.site.register(Comment)
admin.site.register(Reply)