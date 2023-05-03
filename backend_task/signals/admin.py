from django.contrib import admin

# Register your models here.


from signals.models import Client
from signals.models import Artist
from signals.models import Work

# class Signal_Admin(admin.ModelAdmin):

admin.site.register(Client)
admin.site.register(Artist)
admin.site.register(Work)

