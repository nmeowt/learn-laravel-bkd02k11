from django.db import models
from store.models import Product
from django.conf import settings


class Order(models.Model):
    staff = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    code = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    quantity = models.PositiveIntegerField(default=None)

    def __str__(self):
        return '{}'.format(self.id)

    @property
    def get_cost(self):
        return self.price * self.quantity

    @property
    def price_display(self):
        return f'{self.price:.3f}₫'
