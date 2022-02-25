from django.db import models


class Vote(models.Model):
    comment = models.ForeignKey('comments.Comment', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    create_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return f'{self.comment.get_absolute_url()}vote/{self.id}/'
