# Generated by Django 4.1.4 on 2023-05-05 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_chirho', '0006_alter_postchirho_post_chirho_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postchirho',
            name='post_picture_chirho',
            field=models.ImageField(null=True, upload_to='publications_chirho', verbose_name='Subir imagen'),
        ),
    ]
