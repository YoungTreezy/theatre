from django.db import models
from django.urls import reverse

from accounts.models import MyUser
from theatre import settings


class Note(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, null=True)
    description = models.TextField(verbose_name='Текст')
    created = models.DateField(auto_now_add=True, verbose_name='Время добавления')
    update = models.DateField(auto_now=True, verbose_name='Время последнего обновления')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    finish = models.DateField(verbose_name='Дедлайн')

    def get_absolute_url(self):
        return reverse('notes:delete', kwargs={'note_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
