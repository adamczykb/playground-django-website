# Generated by Django 2.2.4 on 2019-08-13 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0011_event_calendar_not_null'),
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aktualnosci',
            name='event',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='schedule.Event'),
        ),
    ]
