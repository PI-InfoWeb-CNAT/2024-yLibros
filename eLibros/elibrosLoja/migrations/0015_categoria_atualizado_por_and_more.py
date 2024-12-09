# Generated by Django 5.1.3 on 2024-12-07 00:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("elibrosLoja", "0014_remove_autor_atualizado_por_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="categoria",
            name="atualizado_por",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="categorias_atualizadas",
                to="elibrosLoja.administrador",
            ),
        ),
        migrations.AddField(
            model_name="historicalcategoria",
            name="atualizado_por",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="elibrosLoja.administrador",
            ),
        ),
        migrations.AlterField(
            model_name="historicalpedido",
            name="numero_pedido",
            field=models.CharField(
                db_index=True, default="165894556750", max_length=12
            ),
        ),
        migrations.AlterField(
            model_name="pedido",
            name="numero_pedido",
            field=models.CharField(
                default="165894556750", max_length=12, primary_key=True, serialize=False
            ),
        ),
    ]
