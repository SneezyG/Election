# Generated by Django 5.0.2 on 2024-02-26 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polling_unit_name', models.CharField(max_length=50)),
                ('party_abbreviation', models.CharField(max_length=4)),
                ('party_score', models.IntegerField()),
                ('user_name', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'new_vote',
            },
        ),
    ]
