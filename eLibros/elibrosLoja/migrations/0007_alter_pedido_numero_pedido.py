# Generated by Django 5.0.3 on 2024-09-02 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elibrosLoja', '0006_alter_pedido_numero_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='numero_pedido',
            field=models.CharField(default='043641522619', max_length=12, primary_key=True, serialize=False),
        ),
    ]
