# Generated by Django 2.2.4 on 2019-08-15 22:19

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20190814_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=200)),
                ('zdjecie', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='images/aktualnosci/')),
            ],
            options={
                'verbose_name_plural': 'Slider ze zdjeciami placówki',
            },
        ),
        migrations.AlterField(
            model_name='aktualnosci',
            name='do_kogo',
            field=models.ManyToManyField(blank=True, to='website.GrupyPrzedszkolne', verbose_name='Gdzie ma być wyswietlana aktualność (domyslnie na głównej)'),
        ),
    ]
