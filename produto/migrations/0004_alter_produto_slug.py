# Generated by Django 3.2.4 on 2021-06-24 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_auto_20210623_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
