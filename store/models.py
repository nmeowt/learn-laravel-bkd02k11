from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True,
                            verbose_name="Tên")
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            unique=True,
                            verbose_name="Đường dẫn")

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'Thể loại'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:product-list-by-category',
                       args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE,
                                 verbose_name="Thể loại")
    name = models.CharField(max_length=200,
                            db_index=True,
                            verbose_name="Tên")
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            verbose_name="Đường dẫn")
    image = models.ImageField(upload_to='products/',
                              blank=True,
                              verbose_name="Ảnh")
    price = models.DecimalField(max_digits=10,
                                decimal_places=0,
                                verbose_name="Giá")
    available = models.BooleanField(default=True,
                                    verbose_name="Còn bán")
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name="Tạo lúc")
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name="Cập nhật lúc")

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'product'
        verbose_name_plural = 'Sản phẩm'

    def __str__(self):
        return self.name

    @property
    def price_display(self):
        return f'{self.price:.3f}₫'
    price_display.fget.short_description = u'Giá'
