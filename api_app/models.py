from django.contrib.auth.models import User
from django.db import models


class AssetHolder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Animal(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class AnimalGrade(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    letter_grade = models.CharField(max_length=200)
    number_grade = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.animal.name} - {self.letter_grade}"


class ValuePoint(models.Model):
    animal_grade = models.ForeignKey(AnimalGrade, on_delete=models.CASCADE)
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.animal_grade} - {self.date}"


class AnimalResource(models.Model):
    owner = models.ForeignKey(AssetHolder, on_delete=models.CASCADE)
    type = models.ForeignKey(AnimalGrade, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.owner} - {self.type}"
