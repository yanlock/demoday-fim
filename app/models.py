from django.db import models
from django.core import validators
from django.contrib.auth.models import (PermissionsMixin, AbstractBaseUser,
    UserManager)
import re

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length = 255,
        unique = True,
        validators = [validators.RegexValidator(re.compile('^[\w.@+-]+$'),
        'O nome de usuário só pode conter letras e digitos.',
        'invalid',
        )],
        verbose_name = 'Nome de usuário',
    )

    nome_completo = models.CharField(
        max_length = 255,
        verbose_name = 'Nome completo',
        blank = True,
    )

    email = models.EmailField(
        max_length = 255,
        unique = True,
        verbose_name = 'E-mail',
    )

    foto_usuario = models.ImageField(
        upload_to = 'users_photos/',
        blank = True,
        verbose_name = 'Foto do Usuário'
    )

    is_active = models.BooleanField(
        default = True,
        blank = True,
        verbose_name = 'Ativo',
    )

    is_staff = models.BooleanField(
        default = False,
        blank = True,
        verbose_name = 'Staff',
    )

    date_joined = models.DateTimeField(
        auto_now_add = True,
        verbose_name = 'Data de entrada',
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


class Receita(models.Model):

    PRATOS = (
        ('Q', 'Quente'),
        ('F', 'Frio'),
    )

    TIPOS_PRATO = (
        ('S', 'Salgado'),
        ('D', 'Doce'),
        ('Vga', 'Vegano'),
        ('Vge', 'Vegetariano'),
    )

    usuario = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
    )

    id_receita = models.AutoField(
        primary_key= True,
        auto_created= True,
        verbose_name = 'ID receita',
        )

    nome_receita = models.CharField(
        max_length = 255,
        verbose_name = 'Nome da receita',
    )

    receita = models.TextField(
        verbose_name = 'Receita',
    )

    descricao_receita = models.CharField(
        max_length = 255,
        verbose_name = 'Descrição da receita',
    )

    ingredientes = models.TextField(
        verbose_name = 'Ingredientes',
    )

    foto_receita = models.ImageField(
        upload_to = 'receitas_fotos/',
        verbose_name = 'Foto da receita',
    )

    prato = models.CharField(
        max_length = 255,
        choices = PRATOS,
        verbose_name = 'Prato',
    )

    tipo_prato = models.CharField(
        max_length = 255,
        choices = TIPOS_PRATO,
        verbose_name = 'Tipo do prato',
    )

    aprovado = models.BooleanField(
        default = False,
        verbose_name = 'Aprovar receita',
    )

    data_criacao = models.DateField(
        auto_now_add = True,
    )

    def __str__(self):
        return self.nome_receita




