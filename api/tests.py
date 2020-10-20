from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Item


class APITests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(username='testuser1', password='abc123')
        testuser1.save()
        testcategory1 = Category.objects.create(name='tripcat')
        testcategory1.save()
        testitem1 = Item.objects.create(name="some trip", description='nice trip', user=testuser1, category=testcategory1)
        testitem1.save()


    def test_item_content(self):
        item = Item.objects.get(id='1')
        self.assertEqual(f'{item.name}', 'testuser1')
        self.assertEqual(f'{item.description}', 'nice trip')

