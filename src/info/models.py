from django.db import models
from django.urls import reverse


class University(models.Model):
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        verbose_name = 'название Университета'
        verbose_name_plural = 'Названия Университетов'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('info:uni_description', kwargs={'university_id': self.pk})


class Actors(models.Model):
    master = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    description = models.TextField()
    university = models.ForeignKey('University', on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, upload_to='photo/%Y/%m/%d')

    class Meta:
        verbose_name = 'мастера'
        verbose_name_plural = 'Мастера'

    def __str__(self):
        return self.master


class Info_about_university(models.Model):
    title = models.CharField(max_length=250)
    university = models.OneToOneField('University', on_delete=models.CASCADE)
    description = models.TextField()

    class Meta:
        verbose_name = 'информация об Университете'
        verbose_name_plural = 'Информация об Университетах'

    def __str__(self):
        return self.title


class GlobalInformation(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255)
    description = models.TextField(verbose_name='Текст')
    photo = models.ImageField(blank=True, upload_to='photo/%Y/%m/%d')
    published = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    university = models.ForeignKey('University', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'глобальная информация'
        verbose_name_plural = 'Глобальная информация'
        ordering = ['-published']
