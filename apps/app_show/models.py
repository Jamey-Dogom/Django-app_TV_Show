from django.db import models

# Create your models here.

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 5:
            errors['title'] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = "Network should be at least 3 characters"
        if len(postData['description']) > 0 and len(postData['description']) < 10:
            errors['description'] = "Description is optional, but if present must be at least 10 characters"
        return errors



class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateField('%m/%d/%Y')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __repr__(self):
        return f"<Show object:  {self.id} {self.title} {self.network} {self.description}>"
