# Generated by Django 5.0.2 on 2024-02-25 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0003_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AnnouncedLGAResults',
        ),
        migrations.DeleteModel(
            name='AnnouncedPuResults',
        ),
        migrations.DeleteModel(
            name='LGA',
        ),
        migrations.DeleteModel(
            name='PollingUnit',
        ),
        migrations.DeleteModel(
            name='Ward',
        ),
    ]
