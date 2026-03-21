from django.contrib import admin
from .models import Projects,Frontend,Backend,Tools

# Register your models here.
admin.site.register(Projects)
admin.site.register(Backend)
admin.site.register(Frontend)
admin.site.register(Tools)