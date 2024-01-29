from django.urls import path
from .views import note_list, add_note, edit_note, delete_note

urlpatterns = [
    path("", note_list, name="note_list"),
    path("add/", add_note, name="add_note"),
    path("edit/<int:pk>/", edit_note, name="edit_note"),
    path("delete/<int:pk>/", delete_note, name="delete_note"),
]
