from django.db import models


def directory_path(instance, filename):
    return f'photos/{instance.title}/{filename}'


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення') #one add at create
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата редагування') #update date every on object update
    photo = models.ImageField(upload_to=directory_path, verbose_name='Фото') #upload_to='photos/%Y/%m/%d/'
    is_published = models.BooleanField(default=True, verbose_name='Опубліковано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категорія')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
        ordering = ['-create_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Назва категорії')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['title']
