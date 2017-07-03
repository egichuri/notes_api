from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker

from api.models import Note
fake = Faker()

class TestApiEndpoints(APITestCase):
    """Test the Api Endpoints"""

    def setUp(self):
        self.notes_endpoint = reverse('note-list')
        create_initial_note = self.client.post(self.notes_endpoint, {'note_content': 'initial note'})
        self.initial_content = Note.objects.first()

        self.initial_note_endpoint = reverse('note-detail', kwargs={'pk': self.initial_content.id})

    def create_multiple_notes(self):
        for count in xrange(8):
            self.client.post(self.notes_endpoint, {'note_content': 'test content {}'.format(count)})

    def test_note_creation(self):

        new_note_response = self.client.post(self.notes_endpoint, {'note_content': 'test content'})
        self.assertEqual(new_note_response.status_code, 201)
        self.assertIn('test content', new_note_response.content)

    def test_note_character_limit(self):
        invalid_note = self.client.post(self.notes_endpoint, {'note_content': fake.text()} )

        self.assertIn('text too long', invalid_note.content)

    def test_note_listing(self):
        get_notes = self.client.get(self.notes_endpoint)

        self.assertEqual(get_notes.status_code, 200)
        self.assertIn('initial note', get_notes.content)

    def test_note_update(self):
        self.client.put(self.initial_note_endpoint, {'note_content': 'updated content'})
        self.initial_content.refresh_from_db()
        self.assertEqual(self.initial_content.note_content, 'updated content')

    def test_note_deletion(self):
        notes_count_before_deletion = Note.objects.count()
        self.client.delete(self.initial_note_endpoint)
        notes_count_after_deletion = Note.objects.count()

        self.assertEqual(notes_count_after_deletion, notes_count_before_deletion - 1)

    def test_pagination(self):
        self.create_multiple_notes()
        all_notes = self.client.get(self.notes_endpoint)
        self.assertEqual(all_notes.data['count'], len(all_notes.data['results']))

        self.create_multiple_notes()
        after_more_notes = self.client.get(self.notes_endpoint)
        self.assertGreater(after_more_notes.data['count'], len(after_more_notes.data['results']))


