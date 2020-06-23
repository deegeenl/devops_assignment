import datetime

from django.test import TestCase


# Create your tests here.
from person.models import Person


class PersonModelTest(TestCase):

    def test_person_created(self):
        p = Person.objects.create(
            name="Dirk",
            dob="1971-05-21"
        )
        self.assertEqual(1, Person.objects.count())

    def test_person_birthday_in_5_days(self):
        today = datetime.date.today()
        today_plus_five = today + datetime.timedelta(days=5)
        dob = today_plus_five.replace(year=1971)
        p = Person.objects.create(
            name="Dirk",
            dob=dob
        )
        self.assertEqual(5, p.days_till_birthday())

    def test_person_birthday_5_days_ago(self):
        today_minus_five = datetime.date.today() - datetime.timedelta(days=5)
        dob = today_minus_five.replace(year=1971)
        p = Person.objects.create(
            name="Dirk",
            dob=dob
        )
        self.assertTrue(p.days_till_birthday() >= 360)


class ViewsTestCase(TestCase):

    def test_creating_person(self):
        response = self.client.put('/hello/Morty', data={'dateOfBirth': '1971-05-21'}, content_type="application/json")
        self.assertEqual(204, response.status_code, f"Response was: {response.content}")
        self.assertEqual(1, Person.objects.count())
        p = Person.objects.first()
        self.assertEqual("Morty", p.name)

    def test_birthday(self):
        dob = datetime.date.today().replace(year=1971)
        Person.objects.create(name="Dirk", dob=dob)
        response = self.client.get('/hello/Dirk')
        self.assertIn("Happy birthday!".lower(), response.json()['message'].lower())

    def test_in_five_days(self):
        dob = datetime.date.today() + datetime.timedelta(days=5)
        dob = dob.replace(year=1971)
        Person.objects.create(name="Dirk", dob=dob)
        response = self.client.get('/hello/Dirk')
        self.assertIn("in 5 days".lower(), response.json()['message'].lower())