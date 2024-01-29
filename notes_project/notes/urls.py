from django.urls import path
from .views import note_list, add_note, edit_note, delete_note

urlpatterns = [
    # URL pattern for displaying the list of notes
    path("", note_list, name="note_list"),
    # URL pattern for adding a new note
    path("add/", add_note, name="add_note"),
    # URL pattern for editing an existing note
    path("edit/<int:pk>/", edit_note, name="edit_note"),
    # URL pattern for deleting an existing note
    path("delete/<int:pk>/", delete_note, name="delete_note"),
]
