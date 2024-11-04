# Generated by Django 3.2 on 2024-11-01 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
                ('texto', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrelocal', models.CharField(max_length=50)),
                ('nombrevisita', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('horapartido', models.DateTimeField()),
                ('comentarios', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eva3.comentario')),
            ],
        ),
    ]
