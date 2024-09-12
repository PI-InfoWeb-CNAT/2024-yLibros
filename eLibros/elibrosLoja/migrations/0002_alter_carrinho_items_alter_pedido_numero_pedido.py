# Generated by Django 5.0.3 on 2024-09-12 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elibrosLoja', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrinho',
            name='items',
            field=models.ManyToManyField(default=None, null=True, related_name='items_do_carrinho', to='elibrosLoja.itemcarrinho'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='numero_pedido',
            field=models.CharField(default='313219997652', max_length=12, primary_key=True, serialize=False),
        ),
    ]
