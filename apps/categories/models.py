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
    url_assign = models.CharField(max_length=64)
    description = models.TextField('Описание')
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/categories/{self.url_assign}/'


class Topic(models.Model):
    title = models.CharField('Название', max_length=255)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField('Описание')
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey('categories.Category', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField('Статус', max_length=32, choices=STATUS)

    class Meta:
        verbose_name = 'Топик'
        verbose_name_plural = 'Топики'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/categories/{self.category.url_assign}/topics/{self.slug}/'
