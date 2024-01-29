from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm


# Displaying the list of notes
@login_required
def note_list(request):
    # Retrieving notes, ordered by date in descending order
    notes = Note.objects.filter(user=request.user).order_by("-date_added")
    return render(request, "notes/note_list.html", {"notes": notes})


# Adding a new note
@login_required
def add_note(request):
    if request.method == "POST":
        # If the request is POST, process the submitted form data
        form = NoteForm(request.POST)
        if form.is_valid():
            # If form is valid, create a new note associated with the logged-in user and redirect to the note list
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect("note_list")
    else:
        # If the request is GET, render the form page with an empty form
        form = NoteForm()
    return render(request, "notes/add_note.html", {"form": form})


# Editing an existing note
def edit_note(request, pk):
    # Retrieving the specific note by primary key
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == "POST":
        # If the request is POST, process the submitted form data
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            # If form is valid, update the note and redirect to the note list
            form.save()
            return redirect("note_list")
    else:
        # If the request is GET, render the form page with the form pre-filled with the note's data
        form = NoteForm(instance=note)
    return render(request, "notes/edit_note.html", {"form": form, "note": note})


# Deleting an existing note
@login_required
def delete_note(request, pk):
    # Retrieve the specific note by primary key
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == "POST":
        # If the request is POST, delete the note and redirect to the note list
        note.delete()
        return redirect("note_list")
    # If the request is GET, render the confirmation page for deleting the note
    return render(request, "notes/delete_note.html", {"note": note})
