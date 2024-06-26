# Generated by Django 5.0.4 on 2024-04-23 22:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('año', models.CharField(max_length=10)),
                ('autor', models.CharField(max_length=50)),
                ('editorial', models.CharField(max_length=50)),
                ('imagen', models.ImageField(upload_to='img_libros')),
                ('disponible', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Libros',
            },
        ),
    ]
