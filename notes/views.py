from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Note
from .forms import NewNote
import uuid


class ViewNote(DetailView):
    model = Note
    template_name = 'notes/view_note.html'


class NewNote(CreateView):
    model = Note
    template_name = 'notes/new_note.html'
    form_class = NewNote
    success_url = reverse_lazy('home:index')

    def form_valid(self, form):
        if super().form_valid(form):
            return redirect('notes:view', pk=self.object.pk)

