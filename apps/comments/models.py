from django.db import models


class Comment(models.Model):
    text = models.TextField('текст комментария')
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    create_at = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey('categories.Topic', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return f'/categories/{self.topic.category.url_assign}/topics/{self.topic.slug}/comments/{self.id}/'
