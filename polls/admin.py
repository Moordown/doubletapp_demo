from django.contrib import admin
from django.utils.safestring import mark_safe
from imagekit.admin import AdminThumbnail

from .models import Category, Level, Theme, Word, Example


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['category_image']

    def category_image(self, obj):
        return mark_safe(f'<img src="{obj.icon}" width=256 height=256 />')


admin.site.register(Level)


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    readonly_fields = ['word_sound']

    def word_sound(self, obj):
        sound_url = obj.sound
        import os
        ext = os.path.splitext(sound_url)[-1]
        if ext != '.mp3':
            return mark_safe(f'<h3>Please, specify mp3 format, for listening in admin record</h3>')
        else:
            return mark_safe(f'<audio controls><source src="{obj.sound}" type="audio/mpeg"></audio>')


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    readonly_fields = ['theme_image']

    def theme_image(self, obj):
        return mark_safe(f'<img src="{obj.photo}" width=256 height=256 />')
