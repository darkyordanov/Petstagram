from django.db import models

from petstagram.photos.models import PetPhoto

class Comment(models.Model):
    MAX_COMMENT_TEXT = 300

    text = models.TextField(
        max_length=MAX_COMMENT_TEXT,
        blank=False,
        null=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    modified_at = models.DateTimeField(
        auto_now=True,
    )

    photo = models.ForeignKey(
        PetPhoto,
        on_delete=models.DO_NOTHING,
    )


class PhotoLike(models.Model):
    pet_photo = models.ForeignKey(
        PetPhoto,
        on_delete=models.DO_NOTHING
    )