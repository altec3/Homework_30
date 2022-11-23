from django.contrib.auth.models import AbstractUser
from django.db import models

from locations.models import Location


class User(AbstractUser):
    ROLE = [
        ("admin", "Администратор"),
        ("member", "Пользователь"),
        ("moderator", "Модератор")
    ]
    role = models.CharField(max_length=9, choices=ROLE, default="member")
    age = models.PositiveSmallIntegerField(null=True)
    location_id = models.ManyToManyField(Location)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['username']

    def __str__(self):
        return self.username

    @property
    def total_ads(self):
        return self.ad_set.filter(is_published=True).count()
