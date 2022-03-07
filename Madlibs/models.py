from django.db import models


# Create your models here.
class Madlib(models.Model):
    def __str__(self):
        return self.person

    id = models.IntegerField(primary_key=True)
    person = models.CharField(max_length=200, default="null")
    noun = models.CharField(max_length=200, default="null")
    superlative_ending_est = models.CharField(max_length=200, default="null")
    body_part = models.CharField(max_length=200, default="null")
    verb_end_ing = models.CharField(max_length=200, default="null")
    verb = models.CharField(max_length=200, default="null")
    event = models.CharField(max_length=200, default="null")
    day_of_week = models.CharField(max_length=200, default="null")
    place = models.CharField(max_length=200, default="null")
    time_span = models.CharField(max_length=200, default="null")
    adverb = models.CharField(max_length=200, default="null")
    number = models.CharField(max_length=200, default="null")
    occupation = models.CharField(max_length=200, default="null")
    adjective = models.CharField(max_length=200, default="null")
    celebrity = models.CharField(max_length=200, default="null")
    verb_end_s = models.CharField(max_length=200, default="null")
    silly_word = models.CharField(max_length=200, default="null")
    last_name = models.CharField(max_length=200, default="null")
    illness = models.CharField(max_length=200, default="null")
    noun_plural = models.CharField(max_length=200, default="null")
    relative = models.CharField(max_length=200, default="null")
    verb_end_ed = models.CharField(max_length=200, default="null")
    amount_of_time = models.CharField(max_length=200, default="null")
    month = models.CharField(max_length=200, default="null")
    company = models.CharField(max_length=200, default="null")
    noun_end_ers = models.CharField(max_length=200, default="null")
    girl_name = models.CharField(max_length=200, default="null")
    boy_name = models.CharField(max_length=200, default="null")
    animal_plural = models.CharField(max_length=200, default="null")
    kitchen_appliance = models.CharField(max_length=200, default="null")
    food_plural = models.CharField(max_length=200, default="null")
    liquid = models.CharField(max_length=200, default="null")
    government_position = models.CharField(max_length=200, default="null")
    holiday = models.CharField(max_length=200, default="null")
    crime = models.CharField(max_length=200, default="null")
    fruit = models.CharField(max_length=200, default="null")
    location = models.CharField(max_length=200, default="null")
    measurement = models.CharField(max_length=200, default="null")
    game = models.CharField(max_length=200, default="null")
    weapon_plural = models.CharField(max_length=200, default="null")
    animal = models.CharField(max_length=200, default="null")






