# Generated by Django 4.2.1 on 2023-05-15 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_chirho', '0011_alter_postchirho_post_picture_chirho'),
    ]

    operations = [
        migrations.AddField(
            model_name='postchirho',
            name='contact_chirho',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Contacto'),
        ),
    ]