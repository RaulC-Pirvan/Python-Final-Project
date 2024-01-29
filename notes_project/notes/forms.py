# Importing necessary modules
from django import forms
from .models import Note


# Defining a Django form named 'NoteForm'
class NoteForm(forms.ModelForm):
    # Meta class to provide additional information about the form
    class Meta:
        # Specifying the model associated with the form
        model = Note

        # Specifying the fields from the model to be included in the form
        fields = ["text"]
