from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True, default='batman.png')

    def __str__(self):
        return f'Profile for user {self.user.username}'



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
