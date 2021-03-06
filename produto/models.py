import os
from PIL import Image
from django.db import models
from django.conf import settings


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(
        upload_to='produtos_imagens/Y%/m%/d%', blank=True, null=True)
    slug = models.SlugField(unique=True)
    preco_marketing = models.FloatField(default=0)
    preco_marketing_promocional = models.FloatField(default=0)
    tipos = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variação'),
            ('S', 'Simples')
        )
    )

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, origin_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return

        new_height = round(new_width * origin_height)/original_width
        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        max_image_size = 800

        if self.imagem:
            self.resize_image(self.imagem, max_image_size)

    def __str__(self):
        return self.nome


"""
Variacao:
    nome - char
    produto - FK Produto
    preco - Float
    preco_promocional - Float
    estoque - Int
"""


class Varicao(Produto):
    pass
