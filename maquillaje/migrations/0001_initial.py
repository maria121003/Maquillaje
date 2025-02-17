# Generated by Django 5.0.6 on 2024-06-15 16:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Brand_owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('publication_year', models.IntegerField()),
                ('nationality', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('varieties', models.CharField(max_length=255)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maquillaje.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Owner_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maquillaje.brand_owner')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maquillaje.product_type')),
            ],
        ),
    ]
