from django.db import models
import uuid

class Link(models.Model):
    id = models.UUIDField(default=uuid.uuid4().hex, primary_key=True)
    path = models.CharField(max_length=200, default=str(uuid.uuid4())[:8])
    destination = models.URLField()

    def __str__(self):
        return "%s" % self.path

