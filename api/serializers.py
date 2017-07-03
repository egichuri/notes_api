from rest_framework import serializers
from api.models import Note

class NoteSerializer(serializers.ModelSerializer):
    """docstring for NoteSerializer"""
     
    class Meta:
        model = Note
        fields = '__all__'

    def validate_note_content(self, value):
        if len(value) > 140:
            raise serializers.ValidationError('Note content text too long')
        return value