# Generated by Django 5.0.1 on 2024-02-02 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=15)),
                ('contraseña', models.CharField(max_length=20)),
            ],
        ),
    ]