from django.test import TestCase
from .models import Todos

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todos.objects.create(title='To do oat face mask', body='sunday')
    
    def test_title_content(self):
        todo = Todos.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'To do oat face mask')

    def test_body_content(self):
        todo = Todos.objects.get(id=1)
        expected_object_name = f'{todo.body}'
        self.assertEquals(expected_object_name, 'sunday')

