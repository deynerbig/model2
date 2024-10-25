# Generated by Django 3.2 on 2024-10-25 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='caballo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('raza', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
                ('velocidad', models.CharField(choices=[('alta', 'alta'), ('media', 'media'), ('baja', 'baja')], max_length=5)),
                ('resistencia', models.CharField(choices=[('alta', 'alta'), ('media', 'media'), ('baja', 'baja')], max_length=5)),
            ],
        ),
    ]
