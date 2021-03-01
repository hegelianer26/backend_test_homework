from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", verbose_name='Автор')
    group = models.ForeignKey('Group', on_delete=models.PROTECT, blank=True, null=True, verbose_name='Группа')

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(max_length=100, unique=True, null=True, verbose_name="URL")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
