from django.contrib import admin

# Register your models here.
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('text_short', 'author', 'created_at')
    list_filter = ('author', 'created_at')

    def text_short(self, obj):
        return obj.text[:50]

    text_short.short_description = 'Text'

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)