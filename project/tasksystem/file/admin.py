from django.contrib import admin
from .models import FileAttachment

# Register your models here.
class FileAttachmentAdmin(admin.ModelAdmin):
    list_display=("file","uploaded_at")
admin.site.register(FileAttachment,FileAttachmentAdmin)
