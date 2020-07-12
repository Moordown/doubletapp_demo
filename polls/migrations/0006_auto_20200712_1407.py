# Generated by Django 3.0.8 on 2020-07-12 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20200712_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=None, upload_to='', verbose_name='Picture')),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.CharField(max_length=256),
        ),
    ]
