from django.db import models
from django.core.validators import MinLengthValidator

from petstagram.pets.models import Pet
from petstagram.photos.validators import MaxSizeValidator, SIZE_5_MB


class PetPhoto(models.Model):
    DESCRIPTION_MAX_LENGTH = 300
    DESCRIPTION_MIN_LENGTH = 10

    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to='pet_photos',
        blank=False,
        null=False,
        validators=(
            MaxSizeValidator(limit_value=SIZE_5_MB),
        )
    )

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LENGTH,
        blank=True,
        null=True,
        validators=(
            MinLengthValidator(DESCRIPTION_MIN_LENGTH),
        )
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        blank=True,
        null=True,
    )

    pets = models.ManyToManyField(
        Pet,
        blank=True,
    )

    created_at = models.DateField(
        auto_now_add=True
    )

    modified_at = models.DateField(
        auto_now=True,
    )