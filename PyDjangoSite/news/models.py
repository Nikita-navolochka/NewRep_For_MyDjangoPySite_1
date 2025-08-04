from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField('Название', max_length=50, default='defolt')
    anons = models.CharField('Анонс', max_length=250, default='defolt')
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')


    def __str__(self):
        return self.title


class Meta:
    verbose_name ='new'
    verbose_name_plural = 'news'
