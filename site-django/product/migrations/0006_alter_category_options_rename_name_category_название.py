# Generated by Django 5.0.4 on 2024-05-13 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_rename_image_category_иконка_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('Название',)},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='Название',
        ),
    ]
