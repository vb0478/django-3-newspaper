# Generated by Django 3.0.7 on 2020-06-11 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, verbose_name='Nazwa Kategorii')),
            ],
            options={
                'verbose_name': 'Kategoria',
                'verbose_name_plural': 'Kategorii',
                'ordering': ['title'],
            },
        ),
    ]
