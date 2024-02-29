from django.db import models
from django.utils.text import slugify


class Pet(models.Model):
    NAME_MAX_LENGTH = 30

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        blank=False,
        null=False,
    )

    pet_photo = models.URLField(
        blank=False,
        null=False,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        null=False,
        editable=False,  # Readonly, only in the Django App, not in the DB
    )

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)

        if not self.slug:  # slugify('My name') -> 'My-name'
            self.slug = slugify(f'{self.name}-{self.pk}')

        super().save(*args, **kwargs)
