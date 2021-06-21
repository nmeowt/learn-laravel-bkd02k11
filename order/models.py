from django.db import models
from store.models import Product
from django.conf import settings


class Order(models.Model):
    staff = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Nhân viên"
    )
    code = models.CharField(max_length=20, verbose_name="Mã")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Tạo lúc")
    updated = models.DateTimeField(auto_now=True, verbose_name="Cập nhật lúc")

    class Meta:
        ordering = ('-created',)
        verbose_name = 'order'
        verbose_name_plural = 'Hóa đơn'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE,
                              verbose_name="Hóa đơn")
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE,
                                verbose_name="Sản phẩm")
    price = models.DecimalField(max_digits=10,
                                decimal_places=0,
                                verbose_name="Giá")
    quantity = models.PositiveIntegerField(default=None,
                                           verbose_name="Số lượng")

    class Meta:
        verbose_name = 'order_item'
        verbose_name_plural = 'Hóa đơn chi tiết'

    def __str__(self):
        return '{}'.format(self.id)

    @property
    def get_cost(self):
        return self.price * self.quantity

    @property
    def price_display(self):
        return f'{self.price:.3f}₫'
