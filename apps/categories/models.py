from django.db import models
from autoslug import AutoSlugField

STATUS = (
    ('draft', 'Черновик'),
    ('enabled', 'Видно'),
    ('disabled', 'Скрыто'),
)


class Category(models.Model):
    title = models.CharField('Название', max_length=255)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField('Описание')
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/categories/{self.slug}/'


class Topic (models.Model):
    title = models.CharField('Название', max_length=255)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField('Описание')
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField('Статус', max_length=32, choices=STATUS)

    def __str__(self):
        return self.title
