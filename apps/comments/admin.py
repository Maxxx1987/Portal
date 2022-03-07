from django.contrib import admin

from apps.comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 1
    readonly_fields = ('user',)



