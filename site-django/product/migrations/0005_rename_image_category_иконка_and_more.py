# Generated by Django 5.0.4 on 2024-05-13 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_image_product_иконка_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='image',
            new_name='Иконка',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='thrumbnail',
            new_name='Картинка',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='slug',
            new_name='Ссылка',
        ),
    ]
