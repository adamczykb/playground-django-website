# Generated by Django 2.2.4 on 2019-08-27 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20190827_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podelementy',
            name='link_do_strony',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.Strona'),
        ),
    ]
