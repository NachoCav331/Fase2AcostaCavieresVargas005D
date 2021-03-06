# Generated by Django 3.1.2 on 2020-10-17 22:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['nombre', 'apellido'],
            },
        ),
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('resumen', models.TextField(max_length=10000)),
                ('isbn', models.CharField(max_length=13, verbose_name='ISBN')),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='boomcomic.autor')),
            ],
        ),
        migrations.CreateModel(
            name='Formato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formatoo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ComicInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID primario de los comics de la tienda', primary_key=True, serialize=False)),
                ('imprimir', models.CharField(max_length=200)),
                ('estado', models.CharField(blank=True, choices=[('p', 'Proximamente'), ('d', 'Disponible'), ('a', 'Agotado')], default='d', help_text='Comic/Manga disponible', max_length=1)),
                ('comic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='boomcomic.comic')),
            ],
        ),
        migrations.AddField(
            model_name='comic',
            name='formato',
            field=models.ManyToManyField(to='boomcomic.Formato'),
        ),
        migrations.AddField(
            model_name='comic',
            name='tipo',
            field=models.ManyToManyField(to='boomcomic.Tipo'),
        ),
    ]
