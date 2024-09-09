# Generated by Django 5.0.3 on 2024-09-02 17:44

import validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elibrosLoja', '0003_pedido_livros_do_pedido_alter_pedido_numero_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='ano_de_publicacao',
            field=models.IntegerField(blank=True, null=True, validators=[validators.nao_e_no_futuro]),
        ),
        migrations.AlterField(
            model_name='livro',
            name='data_de_publicacao',
            field=models.DateField(null=True, validators=[validators.nao_e_no_futuro]),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='numero_pedido',
            field=models.CharField(default='963359090528', max_length=12, primary_key=True, serialize=False),
        ),
    ]