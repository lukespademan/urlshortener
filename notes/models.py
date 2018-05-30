from django.db import models
import uuid

class Note(models.Model):
    id = models.UUIDField(default=uuid.uuid4().hex, primary_key=True)
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=50000)

    def __str__(self):
        return self.title

