from django. db import models
from django.contrib.postgres.fields.array import ArrayField


class Guru(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    services = ArrayField(
        models.CharField(
            max_length=32,
            blank=True,
        ),
        blank=True,
    )
    # ['yoga', 'meditation', 'tennis',]
    bio = models.CharField(max_length=255)
    # store social media handles
    linkedin_handle = models.CharField(max_length=30, null=True)
    instagram_handle = models.CharField(max_length=30, null=True)
    twitter_handle = models.CharField(max_length=30, null=True)
    facebook_handle = models.CharField(max_length=30, null=True)
    # schedule

    # TODO: make Reviews model
    reviews = models.ForeignKey(
        'Reviews',
        on_delete=models.CASCADE,
    )

# yoga_guru = Guru(
#     first_name='Hippie',
#     last_name='Girl',
#     services=['yoga', 'meditation'],
# )
