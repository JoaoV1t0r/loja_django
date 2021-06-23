# Generated by Django 3.2.4 on 2021-06-23 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('status', models.CharField(choices=[('A', 'Aprovado'), ('C', 'Criado'), ('R', 'Reprovado'), ('P', 'Pendente'), ('E', 'Enviado'), ('F', 'Finalizado')], default='C', max_length=255)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto_id', models.PositiveIntegerField()),
                ('produto', models.CharField(max_length=255)),
                ('variacao', models.CharField(max_length=255)),
                ('variacao_id', models.IntegerField()),
                ('preco', models.FloatField()),
                ('preco_promocional', models.FloatField(default=0)),
                ('quantidate', models.PositiveIntegerField()),
                ('imagem', models.CharField(max_length=2000)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedido.pedido')),
            ],
            options={
                'verbose_name': 'Item Pedido',
                'verbose_name_plural': 'Itens do pedido',
            },
        ),
    ]
