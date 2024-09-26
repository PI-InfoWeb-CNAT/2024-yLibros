# Generated by Django 5.0.3 on 2024-09-26 19:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elibrosLoja', '0016_uploadimage_alter_livro_data_de_adicao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='identificacao',
            field=models.CharField(default='Endereço', max_length=30),
        ),
        migrations.AlterField(
            model_name='livro',
            name='data_de_adicao',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 26, 16, 47, 14, 36898)),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='numero_pedido',
            field=models.CharField(default='721204762864', max_length=12, primary_key=True, serialize=False),
        ),
    ]
