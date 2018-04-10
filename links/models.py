from django.db import models
import uuid

class Link(models.Model):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True)
    path = models.CharField(max_length=200, default=str(uuid.uuid4())[:8])
    destination = models.CharField(max_length=200)

    def __str__(self):
        return "%s %s" % (self.path, self.destination)
