from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from product.models import Sale


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'password_repeat']

    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Seu primeiro nome'})
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Seu último nome'})
    )
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Nome de usuário'})
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
    password_repeat = forms.CharField(max_length=255,
                                      widget=forms.PasswordInput(attrs={'placeholder': 'Confirme senha'}))

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name is None:
            raise ValidationError("Precisa preencher o seu nome.")

        return self.cleaned_data.get('first_name')

    def clean_password_repeat(self):
        password = self.cleaned_data.get('password')
        password_repeat = self.cleaned_data.get('password_repeat')

        if self.instance.pk is None and not password_repeat:
            raise ValidationError("Você precisa confirmar sua senha.")
        if password != password_repeat:
            raise ValidationError("Senhas precisam ser iguais.")

        return self.cleaned_data.get('password')


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Seu primeiro nome'})
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Seu último nome'})
    )
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Nome de usuário'})
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name is None:
            raise ValidationError("Precisa preencher o seu nome.")

        return self.cleaned_data.get('first_name')


class UpdateUserPasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password', 'password_repeat']

    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
    password_repeat = forms.CharField(max_length=255,
                                      widget=forms.PasswordInput(attrs={'placeholder': 'Confirme senha'}))

    def save(self, commit=True):
        user = super(UpdateUserPasswordForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}),
                               required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if not user or not user.is_active:
            raise forms.ValidationError("Por algum motivo seu login está inválido.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user


class CheckoutForm(forms.Form):
    sale_product_qtd = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Qtd'}))

    class Meta:
        model = Sale
        fields = ['sale_product_qtd']
