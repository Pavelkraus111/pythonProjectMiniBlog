from django.db import models

class Post(models.Model):

    title = models.CharField('заголовок записи',max_length=100)
    description = models.TextField('Текст записи')
    author = models.CharField('Имя автора',max_length=100)
    data = models.DateField('Дата публикации')
    img = models.ImageField('Изображение', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title},{self.author}'

    class Meta:
        verbose_name = 'Записи'
        verbose_name_plural = 'Записи'

class Comments(models.Model):
    '''Коментарии'''
    email = models.EmailField()
    name = models.CharField('Имя',max_length=50)
    text_comments = models.TextField('Текст комментария', max_length=2000)
    post = models.ForeignKey(Post,verbose_name='Публикация', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name},{self.post}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Коментарии'

class Likes(models.Model):
    '''Лайки'''
    ip = models.CharField('IP-адрес', max_length=100)
    pos = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)
