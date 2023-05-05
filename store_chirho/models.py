import uuid
from django.db import models
from proyectocoderchirho.validators_chirho import image_extension_validator_chirho
from django.contrib.auth.models import User


class PostChirho(models.Model):

    class PostTypeChirho(models.TextChoices):
        COMPUTER_CHIRHO = 'computer_chirho', 'Computadoras'
        GAMING_CHIRHO = 'gaming_chirho', 'Gaming'
        MONITOR_CHIRHO = 'monitor_chirho', 'Monitores'
        NOTEBOOK_CHIRHO = 'notebook_chirho', 'Notebooks'
        TV_CHIRHO = 'tv_chirho', 'Televisores'

    id_chirho = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user_chirho=models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    title_chirho = models.CharField(blank=False, max_length=40, null=False,
        verbose_name='Titulo de la publicación')
    post_type_chirho = models.CharField(
        blank=False, choices=PostTypeChirho.choices, 
        max_length=255, null=False, verbose_name='Tipo publicación')
    post_chirho = models.TextField(blank=False, max_length=400, null=False,
        verbose_name='Descripción de la publicación')
    price_chirho = models.DecimalField(
        db_index=True, decimal_places=2,max_digits=8,
        null=False, verbose_name='Precio en $')
    post_moment_chirho = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Momento Publicado")
    post_picture_chirho = models.ImageField(upload_to='post_photos_chirho', blank=True, null=True, validators=[image_extension_validator_chirho], verbose_name='Subir imagen')
    
    

