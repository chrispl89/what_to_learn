# Generated by Django 5.0.1 on 2024-01-05 19:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Learn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('github_url', models.URLField()),
                ('status', models.CharField(choices=[('adept', 'Never done this before'), ('padawan', 'I wrote some code'), ('jedi', 'I can use it'), ('jedi_master', "I'm expert")], default='adept', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('learn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Learn.learn')),
            ],
        ),
    ]
