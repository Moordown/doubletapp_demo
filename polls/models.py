from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class Category(models.Model):
    name = models.CharField(max_length=64)
    icon = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.code}:{self.name}'


class Theme(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    name = models.CharField(max_length=64)
    photo = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Word(models.Model):
    theme = models.ForeignKey(Theme, related_name='words', on_delete=models.CASCADE)

    name = models.CharField(max_length=64)
    translation = models.CharField(max_length=64)
    transcription = models.CharField(max_length=64)
    example = models.CharField(max_length=128)
    sound = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Example(models.Model):
    """ Example model """

    image = models.ImageField('Picture', default=None)

    image_790x160 = ImageSpecField(
        source='image',
        processors=[ResizeToFill(790, 160)],
        format='JPEG',
        options={'quality': 85}
    )
    ...
