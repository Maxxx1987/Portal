from django.contrib import admin

from apps.categories.models import Category, Topic
from apps.comments.admin import CommentInLine
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class TopicAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget)

    class Meta:
        model = Topic
        fields = '__all__'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url_assign')
    list_display_links = ('title',)



@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status',)
    list_filter = ('title','created_at', 'status')
    search_fields = ('title',)
    inlines = [CommentInLine]
    form = TopicAdminForm
    save_on_top = True


