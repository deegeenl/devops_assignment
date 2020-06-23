from datetime import date

from django.db import models


# Create your models here.
class Person(models.Model):

    name = models.CharField(max_length=200, unique=True)
    dob = models.DateField(verbose_name="Date of Birth")

    def __str__(self):
        return self.name.title()

    def next_birthday(self):
        this_year_birthday = self.dob.replace(year=date.today().year)
        if this_year_birthday < date.today():
            return self.dob.replace(year=date.today().year + 1)
        else:
            return this_year_birthday

    def days_till_birthday(self):
        return (self.next_birthday() - date.today()).days

