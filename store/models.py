from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField('Наименование товара', max_length=255)
    slug = models.SlugField('Slug', max_length=255)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='images/', null=False)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name='Производитель')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')

class Category(MPTTModel):
    name = models.CharField('Категория', max_length=100)
    slug = models.SlugField('Slug', max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

class Company(models.Model):
    name = models.CharField('Компания', max_length=50)
    slug = models.SlugField('Slug', max_length=50)

class StarRating(models.Model):
    value = models.SmallIntegerField('Значение', default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    star = models.ForeignKey('StarRating', on_delete=models.CASCADE, verbose_name='Звезда')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт')

    def __str__(self):
        return f'{self.user} --- {self.star} --- {self.product}'
    
    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

class Review(MPTTModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    text = models.TextField('Комеентарий', max_length=2000)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт')

    def __str__(self):
        return f'{self.id} --- {self.user} --- {self.product}'

class Attribute(models.Model):
    name = models.CharField('Название', max_length=50)
    slug = models.SlugField('Slug', max_length=50)

    def __str__(self):
        return self.name
    
class AttributesValue(models.Model):
    value = models.CharField('Значение', max_length=200)
    slug = models.SlugField('Slug', max_length=200)
    attribute = models.ForeignKey('Attribute', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)