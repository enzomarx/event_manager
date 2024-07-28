from django.test import TestCase
from .models import Event

class EventModelTest(TestCase):
    def setUp(self):
        Event.objects.create(name="Test Event", date="2024-07-28")

    def test_event_creation(self):
        event = Event.objects.get(name="Test Event")
        self.assertEqual(event.name, "Test Event")
        self.assertEqual(str(event.date), "2024-07-28")
