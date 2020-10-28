from django.db import models
from django.contrib.auth import get_user_model

User= get_user_model()


class Product(models.Model):

    name=models.CharField(max_length=250, verbose_name='Наименование')
    slug=models.SlugField(unique=True)
    image=models.ImageField(verbose_name='Изображение')
    description= models.TextField(verbose_name='Описание', null=True)
    price= models.DecimalField(max_digits=9,decimal_places=2,verbose_name='Цена')

    def __str__(self):
        return  self.name


class CartProduct(models.Model):

    user= models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart= models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE,related_name='related_product')
    product=models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    qty= models.PositiveIntegerField(default=1)
    final_price= models.DecimalField(max_digits=9,decimal_places=2, verbose_name='Цена')
    def __str__(self):
        return 'Продукт: {} (дял корзины)'.format(self.product.name)

class Cart(models.Model):

    owner=models.ForeignKey("Customer", verbose_name='Владелец', on_delete=models.CASCADE)
    product= models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products= models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9,decimal_places=2, verbose_name='Общая цена')



    def __str__(self):
        return str(self.id)

class Customer(models.Model):

    user=models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return "Покупатель: {}".format(self.user)


