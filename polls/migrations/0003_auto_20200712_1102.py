# Generated by Django 3.0.8 on 2020-07-12 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200712_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='photo',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='word',
            name='example',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='word',
            name='sound',
            field=models.CharField(max_length=256),
        ),
    ]
