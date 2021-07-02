from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class ErrManager(models.Manager):
    def req_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "The 'title' field is required."
        if len(postData['release_date']) < 1:
            errors['release_date'] = "Th 'releaes date' field is required."
        if len(postData['description']) !=0 and len(postData['description']) < 10:
            errors['description'] = "The 'description' field, if included, must be more than 10 characters."
        return errors

class Network(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __repr__(self):
        return "Network: {}".format(self.name)

class Show(models.Model):
    title = models.CharField(max_length=50)
    network = models.ForeignKey(Network, related_name="shows", on_delete=models.CASCADE)
    release_date = models.CharField(max_length=15, default="2001-10-19")
    description = models.TextField(default="N/A")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ErrManager()

