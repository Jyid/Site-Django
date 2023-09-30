from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=55)
    age = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.last_name} {self.email} ({self.age})'


class Subject(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person')
    name2 = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name2)


class Sub(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'
