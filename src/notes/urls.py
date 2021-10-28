from django.urls import path
from .views import (add_note_view, notes_view)


urlpatterns = [
    path('add_note/', add_note_view, name='add_note'),
    path('', notes_view, name='notes'),
]
