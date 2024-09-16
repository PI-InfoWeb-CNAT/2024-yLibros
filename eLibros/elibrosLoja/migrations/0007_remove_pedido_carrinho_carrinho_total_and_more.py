# Generated by Django 5.0.9 on 2024-09-14 22:01

import datetime
import validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elibrosLoja', '0006_alter_endereco_cep_alter_pedido_numero_pedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='carrinho',
        ),
        migrations.AddField(
            model_name='carrinho',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='livro',
            name='data_de_adicao',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 14, 19, 1, 14, 303306)),
        ),
        migrations.AddField(
            model_name='livro',
            name='qtd_vendidos',
            field=models.IntegerField(default=0, validators=[validators.nao_negativo]),
        ),
        migrations.AddField(
            model_name='livro',
            name='subtitulo',
            field=models.CharField(max_length=200, null=True, validators=[validators.verificar_vazio]),
        ),
        migrations.AddField(
            model_name='pedido',
            name='itens',
            field=models.ManyToManyField(related_name='itens_do_pedido', to='elibrosLoja.itemcarrinho'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='numero_pedido',
            field=models.CharField(default='276922917189', max_length=12, primary_key=True, serialize=False),
        ),
    ]
