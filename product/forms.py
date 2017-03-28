from django import forms

from product.models import Product


class ProductForm(forms.ModelForm):
    product_name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Nome do item'})
    )
    product_url_image = forms.URLField(
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Url da imagem do item'})
    )
    product_description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Descrição do item'}))
    product_qtd = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Quantidade'}))
    product_price = forms.DecimalField(widget=forms.TextInput(attrs={'placeholder': 'R$ Valor'}))
    pub_date = forms.DateTimeField(required=False)

    class Meta:
        model = Product
        fields = ['product_name', 'product_url_image', 'product_description', 'product_price', 'product_qtd']
