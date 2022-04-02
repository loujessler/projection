from django.contrib import admin
from .models import Frame


@admin.register(Frame)
class FrameAdmin(admin.ModelAdmin):
    pass
 