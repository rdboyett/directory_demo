from __future__ import unicode_literals
import re

from django.core.urlresolvers import reverse
from django.db import models
# this auto-creates "created" and "modified" datetime fields for our model
from django_extensions.db.models import (TimeStampedModel)


from bootstrap_project.users.models import User


class DirectoryUser(TimeStampedModel, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    phoneExt = models.CharField(max_length=5, blank=True)
    room = models.CharField(max_length=10, blank=True)
    subject = models.CharField(max_length=65, blank=True)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name + self.user.last_name

    def get_absolute_url(self):
        return reverse('directory:detail', kwargs={'pk': self.pk})