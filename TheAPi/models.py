from django.db import models
from django.contrib.auth.models import User

class Palette(models.Model):
    # A palette has one or two dominant colors
    dominant_color_1 = models.CharField(max_length=6) # Hex code of the color, e.g. "FF0000" for red
    dominant_color_2 = models.CharField(max_length=6, blank=True, null=True) # Optional second dominant color
    # A palette has two to four accent colors
    accent_color_1 = models.CharField(max_length=6)
    accent_color_2 = models.CharField(max_length=6)
    accent_color_3 = models.CharField(max_length=6, blank=True, null=True) # Optional third accent color
    accent_color_4 = models.CharField(max_length=6, blank=True, null=True) # Optional fourth accent color
    # A palette has a name
    name = models.CharField(max_length=50)
    # A palette belongs to a user who created it
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="palettes")
    # A palette can be public or private
    is_public = models.BooleanField(default=False)
    # A palette can be favorited by many users
    favorites = models.ManyToManyField(User, related_name="favorites", blank=True)

    def __str__(self):
        return self.name
