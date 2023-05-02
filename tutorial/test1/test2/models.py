from django.db import models

# Create your models here.
class Profile(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name='Внешний ID пользователя',
        )
    name = models.TextField(
        verbose_name='Имя пользователя',
        )

    def __str__(self):
        return f'#{self.external_id} {self.name}'
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

class Message(models.Model):
    profile = models.ForeignKey(
        to='test2.Profile',
        verbose_name='Профиль',
        on_delete=models.PROTECT,
        )
    text = models.TextField(
        verbose_name='Текст',
        )
    textrus = models.TextField(
        verbose_name='кошка',
    )
    texteng = models.TextField(
        verbose_name='cat',
    )
    lecturename = models.TextField(
        verbose_name='-1',
    )
    created_at = models.DateTimeField(
        verbose_name='Время получения',
        auto_now_add=True,
        )
    def __str__(self):
        return f'Сообщение {self.pk} от {self.profile}'
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
