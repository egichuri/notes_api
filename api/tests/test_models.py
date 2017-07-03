from __future__ import unicode_literals

from django.test import TestCase
from api.models import Note

class TestAppModels(TestCase):
    """tests for the models"""

    def test_note_can_be_created(self):
        object_count_before = Note.objects.count()
        new_note = Note.objects.create(note_content='sample note content')
        object_count_after = Note.objects.count()

        self.assertEqual(object_count_after, object_count_before + 1)