# Generated by Django 2.2.3 on 2019-07-26 11:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0009_auto_20190726_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupyprzedszkolne',
            name='rodzice',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
