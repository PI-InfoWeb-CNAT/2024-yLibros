# Generated by Django 5.1.3 on 2024-12-08 01:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("elibrosLoja", "0016_remove_categoria_atualizado_por_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="carrinho",
            name="data_de_atualizacao",
        ),
        migrations.RemoveField(
            model_name="carrinho",
            name="data_de_cadastro",
        ),
        migrations.RemoveField(
            model_name="categoria",
            name="data_de_atualizacao",
        ),
        migrations.RemoveField(
            model_name="categoria",
            name="data_de_cadastro",
        ),
        migrations.RemoveField(
            model_name="cupom",
            name="data_de_atualizacao",
        ),
        migrations.RemoveField(
            model_name="cupom",
            name="data_de_cadastro",
        ),
        migrations.RemoveField(
            model_name="endereco",
            name="data_de_atualizacao",
        ),
        migrations.RemoveField(
            model_name="endereco",
            name="data_de_cadastro",
        ),
        migrations.RemoveField(
            model_name="generoliterario",
            name="data_de_atualizacao",
        ),
        migrations.RemoveField(
            model_name="generoliterario",
            name="data_de_cadastro",
        ),
        migrations.RemoveField(
            model_name="historicalcarrinho",
            name="data_de_atualizacao",
        ),
        migrations.RemoveField(
            model_name="historicalcarrinho",
            name="data_de_cadastro",
        ),
        migrations.RemoveField(
            model_name="historicalcategoria",
            name="data_de_atualizacao",
        ),
        migrations.RemoveField(
            model_name="historicalcategoria",
            name="data_de_cadastro",
        ),
        migrations.RemoveField(
            model_name="historicalcupom",
            name="data_de_atualizacao",
        ),
        migrations.RemoveField(
            model_name="historicalcupom",
            name="data_de_cadastro",
        ),
        migrations.RemoveField(
            model_name="historicalendereco",
            name="data_de_atualizacao",
        ),
        migrations.RemoveField(
            model_name="historicalendereco",
            name="data_de_cadastro",
        ),
        migrations.RemoveField(
            model_name="historicalgeneroliterario",
            name="data_de_atualizacao",
        ),
        migrations.RemoveField(
            model_name="historicalgeneroliterario",
            name="data_de_cadastro",
        ),
        migrations.RemoveField(
            model_name="historicalitemcarrinho",
            name="data_de_atualizacao",
        ),
        migrations.RemoveField(
            model_name="historicalitemcarrinho",
            name="data_de_cadastro",
        ),
        migrations.RemoveField(
            model_name="historicalpedido",
            name="atualizado_por",
        ),
        migrations.RemoveField(
            model_name="historicalpedido",
            name="data_de_atualizacao",
        ),
        migrations.RemoveField(
            model_name="historicalpedido",
            name="data_de_cadastro",
        ),
        migrations.RemoveField(
            model_name="itemcarrinho",
            name="data_de_atualizacao",
        ),
        migrations.RemoveField(
            model_name="itemcarrinho",
            name="data_de_cadastro",
        ),
        migrations.RemoveField(
            model_name="pedido",
            name="atualizado_por",
        ),
        migrations.RemoveField(
            model_name="pedido",
            name="data_de_atualizacao",
        ),
        migrations.RemoveField(
            model_name="pedido",
            name="data_de_cadastro",
        ),
        migrations.AlterField(
            model_name="historicalendereco",
            name="history_user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="elibrosLoja.administrador",
            ),
        ),
        migrations.AlterField(
            model_name="historicalpedido",
            name="numero_pedido",
            field=models.CharField(
                db_index=True, default="729773149991", max_length=12
            ),
        ),
        migrations.AlterField(
            model_name="pedido",
            name="numero_pedido",
            field=models.CharField(
                default="729773149991", max_length=12, primary_key=True, serialize=False
            ),
        ),
    ]
