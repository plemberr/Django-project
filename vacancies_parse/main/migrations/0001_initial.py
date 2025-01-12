# Generated by Django 5.1.4 on 2025-01-11 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок страницы')),
                ('description', models.TextField(blank=True, verbose_name='Описание страницы')),
            ],
            options={
                'verbose_name': 'Общая статистика',
                'verbose_name_plural': 'Общая статистика',
            },
        ),
        migrations.CreateModel(
            name='StatisticsSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название раздела')),
                ('table_html', models.TextField(verbose_name='HTML таблица')),
                ('graph', models.ImageField(upload_to='statistics/graphs/', verbose_name='График')),
                ('general_statistics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='main.generalstatistics', verbose_name='Общая статистика')),
            ],
            options={
                'verbose_name': 'Раздел статистики',
                'verbose_name_plural': 'Разделы статистики',
            },
        ),
    ]
