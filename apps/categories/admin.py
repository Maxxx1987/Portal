from django.contrib import admin

from apps.categories.models import Category, Topic


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass
