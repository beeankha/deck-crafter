# Generated by Django 2.1.7 on 2019-03-09 22:40

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), help_text='Use a comma to separate tags in the edit form field.', size=None)),
                ('text', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='')),
                ('artist', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='edition',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deck_crafter.Game'),
        ),
        migrations.AddField(
            model_name='card',
            name='edition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deck_crafter.Edition'),
        ),
    ]
