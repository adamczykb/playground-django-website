# Generated by Django 2.2.3 on 2019-08-03 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_auto_20190803_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podelementy',
            name='tytul',
            field=models.TextField(default='', verbose_name='Napis na elemencie'),
        ),
    ]
