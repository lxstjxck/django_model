import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab_project.settings")
django.setup()

from django.test import TestCase, Client
import sys
import os

main_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(main_root)

from main.models import Publisher

class PublisherTestCase(TestCase):
    # создание нового объекта перед каждым новым тестом
    def setUp(self):
        self.publ = Publisher.objects.create(name = "Drofa", address = "Bolshaya Sadovaya, 1",
city = "Moscow", state_province = "Shelepixa", country = "Russia", website = "http://t.me")
        
    # удаление созданного объекта
    def tearDown(self):
        self.publ=None

    # объект строковый?
    def testObject(self):
        self.assertEqual(str(self.publ), "Drofa")

    # объект сохранен?
    def testSaveObject(self):
        self.publ.save()
        obj=Publisher.objects.get(name="Drofa")
        self.assertEqual(obj.name, "Drofa")

    # объект удален?
    def testDeleteObject(self):
        self.publ.save()
        Publisher.objects.filter(name="Drofa").delete()
        self.assertNotEqual(Publisher.objects.filter(name="Drofa"), 'Drofa')

class TemplateTestCase(TestCase):
    # создание тестового клиента
    def setUp(self):
        self.client = Client()
    
    # удаление клиента
    def tearDown(self):
        self.cleint = None

    # проверка страницы books
    def test_book_template(self):
        response = self.client.get("/books/")
        self.assertContains(response, "Author", status_code=200)
        self.assertTemplateUsed(response, "books.html")