from django.contrib import admin

from iutapp.models import Contact, Personnel


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('lastname','surname','slug')

admin.site.register(Contact,ContactAdmin)

class PersonnelAdmin(admin.ModelAdmin):
    list_display = ('nom','prenom','photo','qualite','description')

admin.site.register(Personnel,PersonnelAdmin)