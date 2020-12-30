from django.contrib.auth.models import User
from django.db import models



class Comments(models.Model):

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='my_books')
    text = models.TextField(max_length=600)
    date = models.DateTimeField(auto_now_add=True, null=True)
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.text}'

    # def get_absolute_url(self):
    #     return reverse('comment_list')
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Коментарии'


class LinksThemes(models.Model):
    theme = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.theme}'

    class Meta:
        verbose_name = 'Тема для ссылки'
        verbose_name_plural = 'Темы для ссылок'


class Links(models.Model):

    draft = models.BooleanField(default=True)
    description = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    theme = models.ForeignKey(LinksThemes, on_delete=models.CASCADE, 
        null=True, related_name='child')
    
    def __str__(self):
        return f'{self.description}'

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'