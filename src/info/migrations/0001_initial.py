# Generated by Django 3.2.7 on 2021-10-24 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'название Университета',
                'verbose_name_plural': 'Названия Университетов',
            },
        ),
        migrations.CreateModel(
            name='Info_about_university',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('university', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='info.university')),
            ],
            options={
                'verbose_name': 'информация об Университете',
                'verbose_name_plural': 'Информация об Университетах',
            },
        ),
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('master', models.CharField(max_length=250)),
                ('slug', models.SlugField(blank=True, max_length=250, unique=True)),
                ('description', models.TextField()),
                ('photo', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.university')),
            ],
            options={
                'verbose_name': 'мастера',
                'verbose_name_plural': 'Мастера',
            },
        ),
    ]
