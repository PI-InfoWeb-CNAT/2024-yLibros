# Generated by Django 5.1.3 on 2024-12-06 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "accounts",
            "0004_remove_usuario_endereco_remove_usuario_outro_genero_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="CPF",
            field=models.CharField(default="000.000.000-00", max_length=14),
        ),
        migrations.AlterField(
            model_name="usuario",
            name="dt_nasc",
            field=models.DateField(
                default="2000-01-01", verbose_name="Data de Nascimento"
            ),
        ),
        migrations.AlterField(
            model_name="usuario",
            name="genero",
            field=models.CharField(
                choices=[
                    ("F", "Feminino"),
                    ("M", "Masculino"),
                    ("NB", "Não-binário"),
                    ("PND", "Prefiro não dizer"),
                ],
                default="F",
                max_length=20,
                verbose_name="Identidade de gênero",
            ),
        ),
        migrations.AlterField(
            model_name="usuario",
            name="nome",
            field=models.CharField(default="Nome Completo", max_length=100),
        ),
        migrations.AlterField(
            model_name="usuario",
            name="telefone",
            field=models.CharField(default="(00) 00000-0000", max_length=15),
        ),
    ]
