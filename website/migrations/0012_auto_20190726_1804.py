# Generated by Django 2.2.3 on 2019-07-26 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_delete_rodzicedogrupy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elementy',
            name='flaga_elementu',
        ),
        migrations.AlterField(
            model_name='elementy',
            name='ID',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='elementy',
            name='nazwa_elementu',
            field=models.CharField(max_length=255, verbose_name='Element statyczny strony głównej !nie zmieniać!'),
        ),
        migrations.AlterField(
            model_name='elementy',
            name='nazwa_uzytkownika_elementu',
            field=models.CharField(max_length=255, verbose_name='Napis na elemencie'),
        ),
        migrations.AlterField(
            model_name='podelementy',
            name='powiazanie_z_elementem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='website.Elementy', verbose_name='Z jakim elementem wspolpracuje'),
        ),
        migrations.DeleteModel(
            name='NrElementowGlownych',
        ),
    ]
