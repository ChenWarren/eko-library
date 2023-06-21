from django.test import TestCase
from catalog.models import Author

# Create your tests here.
class AuthorModelTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    Author.objects.create(first_name='Big', last_name='Bob')

  def test_first_name_label(self):
    author = Author.objects.get(id=1)
    field_label = author._meta.get_field('first_name').verbose_name
    self.assertEqual(field_label, 'first name')

  def test_date_of_death_label(self):
    author = Author.objects.get(id=1)
    field_label = author._meta.get_field('date_of_death').verbose_name
    self.assertEqual(field_label, 'Died')