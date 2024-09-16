# Generated by Django 5.0.9 on 2024-09-14 22:59

import datetime
import validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elibrosLoja', '0008_alter_carrinho_items_alter_livro_data_de_adicao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='livro',
            name='data_de_adicao',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 14, 19, 59, 25, 876004)),
        ),
        migrations.AlterField(
            model_name='livro',
            name='subtitulo',
            field=models.CharField(blank=True, max_length=200, null=True, validators=[validators.verificar_vazio]),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='numero_pedido',
            field=models.CharField(default='846512853490', max_length=12, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='livro',
            name='categoria',
            field=models.ManyToManyField(related_name='Categoria_do_Livro', to='elibrosLoja.categoria'),
        ),
    ]
