from django.db import models


class Category(models.Model):
    """ Product category model """
    category_name = models.CharField(verbose_name='Name', max_length=200, db_index=True)
    category_slug = models.SlugField(verbose_name='Slug', max_length=200, db_index=True, unique=True)

    class Meta:
        db_table = 'category'
        ordering = ('category_name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name


class Product(models.Model):
    """ Product model """
    product_name = models.CharField(verbose_name='Name', max_length=200, db_index=True)
    product_slug = models.SlugField(verbose_name='Slug', max_length=200, db_index=True)
    product_image = models.ImageField(verbose_name='Image', upload_to='products/%Y/%m/%d', blank=True)
    product_description = models.TextField(verbose_name='Description', blank=True)
    product_price = models.DecimalField(verbose_name='Price', max_digits=10, decimal_places=2)
    product_stock = models.PositiveIntegerField(verbose_name='Stock')
    product_available = models.BooleanField(verbose_name='Available', default=True)
    product_created = models.DateTimeField(verbose_name='Created', auto_now_add=True)
    product_updated = models.DateTimeField(verbose_name='Updated', auto_now=True)

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'
        ordering = ('product_name',)
        index_together = (('product_slug', 'id'),)

    def __str__(self):
        return self.product_name

