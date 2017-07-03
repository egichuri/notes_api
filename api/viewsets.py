from rest_framework import viewsets
from api.models import Note
from api.serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    """NoteViewSet - for the note model"""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer