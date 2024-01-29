# Importing necessary modules
from django.db import models
from django.contrib.auth.models import User


# Defining a Django model named 'Note'
class Note(models.Model):
    # Define a foreign key relationship with the built-in User model
    # on_delete=models.CASCADE ensures that if a user is deleted,
    # all associated notes will also be deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Date and time when the note is created, set to the current timestamp
    date_added = models.DateTimeField(auto_now_add=True)

    # Text field to store the content of the note
    text = models.TextField()

    # Define a human-readable representation of the Note model
    def __str__(self):
        return f"{self.user.username} - {self.date_added}"
