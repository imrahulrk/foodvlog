# Generated by Django 3.2.16 on 2023-02-24 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_products_available'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categ',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]