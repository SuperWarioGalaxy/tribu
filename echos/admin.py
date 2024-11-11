from django.contrib import admin

from echos.models import Echo


# Register your models here.
@admin.register(Echo)
class EchoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'content',
        'created_at',
        'updated_at',
        'user',
    ]
