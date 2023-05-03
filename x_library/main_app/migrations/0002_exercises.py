# Generated by Django 4.2 on 2023-05-02 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sets', models.IntegerField()),
                ('reps', models.IntegerField()),
                ('distance', models.IntegerField()),
                ('yoga_flow', models.IntegerField()),
            ],
        ),
    ]
