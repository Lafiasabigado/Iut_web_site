# Generated by Django 5.0.6 on 2024-05-21 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='Id')),
                ('lastname', models.CharField(max_length=300, unique=True, verbose_name='Nom')),
                ('surname', models.CharField(max_length=300, unique=True, verbose_name='Prénoms')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('date_post', models.DateTimeField(auto_now=True, verbose_name='Date de Post')),
                ('date_of_birthday', models.DateField(blank=True, null=True, verbose_name='Date de création')),
                ('content', models.TextField(verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Contact',
                'ordering': ['-date_post'],
            },
        ),
    ]