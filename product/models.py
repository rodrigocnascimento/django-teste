from django.db import models
from django.db.models import Sum, F
from django.contrib.auth.models import User


class Product(models.Model):
    user = models.ForeignKey(User)
    product_name = models.CharField(max_length=200, verbose_name="Nome do produto")
    product_url_image = models.URLField(verbose_name="URL do produto")
    product_description = models.TextField(verbose_name="Descrição do produto")
    product_qtd = models.IntegerField(default=0, verbose_name="QTD")
    product_price = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name="Preço")
    pub_date = models.DateTimeField(auto_now_add=True,verbose_name="Data de cadastro")

    def __str__(self):
        return self.product_name

    def user_fullname(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)


class Sale(models.Model):
    product = models.ForeignKey(Product)
    buyer = models.ForeignKey(User, null=True, related_name='buyer')
    seller = models.ForeignKey(User, null=True, related_name='seller')
    sale_product_qtd = models.IntegerField(default=0)
    sale_product_price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    sale_date = models.DateTimeField(auto_now_add=True)

    def buyer_fullname(self):
        return "%s %s" % (self.buyer.first_name, self.buyer.last_name)

    def seller_fullname(self):
        return "%s %s" % (self.seller.first_name, self.seller.last_name)

    def total_sale(self):
        return "%.2f" % (self.sale_product_qtd * self.sale_product_price)

    def __str__(self):
        return self.product.product_name

    def get_user_selled_items(self, seller_id):
        return self.objects.filter(seller_id=seller_id).annotate(
            total=Sum(F('sale_product_qtd') * F('sale_product_price'), output_field=models.FloatField()))

    def get_user_bought_items(self, buyer_id):
        return self.objects.filter(buyer_id=buyer_id).annotate(
            total=Sum(F('sale_product_qtd') * F('sale_product_price'), output_field=models.FloatField()))
