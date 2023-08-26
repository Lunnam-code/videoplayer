from django.db import models

class Video(models.Model):
  name = models.TextField()
  file = models.FileField(upload_to="documents")
  image = models.ImageField(upload_to="documents/images")

  def __str__(self):
    return self.name
