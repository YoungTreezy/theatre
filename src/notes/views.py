from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView

from accounts.models import MyUser
from .models import Note
from .forms import AddNoteForm


def add_note_view(request, pk):
    if request.method == "POST":
        form = AddNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect('/')
    else:
        form = AddNoteForm()
    context = {'form': form}
    return render(request, 'notes/add_note.html', context)


def notes_view(request, pk):
    qs = Note.objects.filter(author=pk)
    return render(request, 'notes/notes.html', {'qs': qs})
