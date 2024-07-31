from django.contrib import admin
from .models import Student
from django.contrib.sessions.models import Session


admin.site.register(Student)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['session_key', 'session_data', 'expire_date']

admin.site.register(Session, SessionAdmin)