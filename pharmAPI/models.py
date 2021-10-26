from django.db import models
from django.db.models.deletion import CASCADE
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])
# Create your models here.



class Types(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(verbose_name="description")

    def __str__(self):
        return self.name


class Drugs(models.Model):
    STATE = (
        ("A", "Available"),
        ("U", "Unavailable")
    )
    types = models.ForeignKey(Types, verbose_name='Class', on_delete=CASCADE)
    name = models.CharField(max_length=100)
    indications = models.TextField()
    contraindications = models.TextField()
    price = models.IntegerField()
    status = models.CharField(max_length=1, choices=STATE)

    def __str__(self):
        return self.name

