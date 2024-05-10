from django.db import models

from django.utils.translation import gettext_lazy as _


class SupplierLevel(models.TextChoices):
    FACTORY = 'factory', _('factory')
    RETAIL_NETWORK = 'retail_network', _('retail_network')
    SOLE_TRADER = 'sole_trader', _('sole_trader')


class Supplier(models.Model):
    level = models.CharField(max_length=15, choices=SupplierLevel.choices)
    name = models.CharField(max_length=50, verbose_name='название')
    email = models.EmailField(verbose_name='электронная почта')
    country = models.CharField(max_length=50, verbose_name='страна')
    city = models.CharField(max_length=40, verbose_name='город')
    street = models.CharField(max_length=60, verbose_name='улица')
    house_number = models.CharField(max_length=10, verbose_name='номер дома')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'поставщик'
        verbose_name_plural = 'поставщики'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название продукта')
    model = models.CharField(max_length=100, verbose_name='модель продукта')
    release_date = models.DateField(verbose_name='дата выхода продукта')

    def __str__(self):
        return f'{self.name} {self.model}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)


class NetworkLink(models.Model):
    contacts = models.ForeignKey('Supplier', on_delete=models.CASCADE, verbose_name='контакты',
                                 related_name='contacts')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='продукт')
    supplier = models.ForeignKey('Supplier', on_delete=models.SET_NULL, blank=True, null=True,
                                 verbose_name='поставщик', related_name='supplier')
    debt_to_supplier = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True,
                                           verbose_name='задолженность')
    time_of_creation = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='время создания')

    def __str__(self):
        return f'{self.contacts.name} - {self.product.name} {self.product.model}'

    class Meta:
        verbose_name = 'звено сети'
        verbose_name_plural = 'звенья сети'
        ordering = ('contacts__name',)
