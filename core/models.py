from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.FloatField()

    class Meta:
        verbose_name = "Товары"
        verbose_name_plural = "Товары"
        ordering = ["-price"]
