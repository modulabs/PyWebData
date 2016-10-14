from django.db import models


class Files(models.Model):
    filename = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.filename


class Colors(models.Model):
    file = models.ForeignKey(Files)
    rgb = models.CharField(max_length=7)

    red = models.IntegerField()
    green = models.IntegerField()
    blue = models.IntegerField()

    def _unicode_(self):
        return self.rgb
    def __str__(self):
        return  self.file.filename

class Personality(models.Model):
    rgb = models.CharField(max_length=7)
    color=models.CharField(max_length=10)
    red = models.IntegerField()
    green = models.IntegerField()
    blue = models.IntegerField()

    description = models.TextField()

    def __str__(self):
        return self.color
