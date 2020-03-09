from django.db import models
from django.utils import timezone

gender_choices = [
    ('Male', "Male"),
    ('Female', "Female")
]

question_choices = [
    (None, ""),
    ('Yes', "Yes"),
    ('No', "No")
]

improve_choices = [
    ('Welcome', "Welcome"),
    ('Room', "Room"),
    ('Food', "Food"),
    ('Guiding', "Guiding")
]

welcome_choices = [
    ('Check-in', "Check-in"),
    ('Waiter', "Waiter"),
]
room_choices = [
    ('Cleanness', "Cleanness"),
    ('Bed', "Bed"),
    ('Bathroom', "Bathroom"),
]
food_choices = [
    ('Breakfast', "Breakfast"),
    ('Lunch', "Lunch"),
    ('Dinner', "Dinner"),
]
guiding_choices = [
    ('Kindness', "Kindness"),
    ('Knowledge', "Knowledge"),
    ('Vehichle', "Vehichle"),
]


class QuestionnaireResponse(models.Model):
    
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10,choices=gender_choices,default="Male")
    age = models.IntegerField()
    nationality = models.CharField(max_length=50)

    question_1 = models.CharField("Has your trip exceeded your expectations?",max_length=5,choices=question_choices,blank=False,default="")
    question_2 = models.TextField("What was the most memorable moment with us?", max_length=200,blank=True)
    question_3 = models.CharField("Where can we improve?",max_length=20, choices=improve_choices, blank=True,default="")

    
    question_3_subquestion_1 = models.CharField("Welcome improvements",max_length=50,choices=welcome_choices, blank=True, default="")
    question_3_subquestion_2 = models.CharField("Room improvements",max_length=50,choices=room_choices, blank=True, )
    question_3_subquestion_3 = models.CharField("Food improvements",max_length=50,choices=food_choices, blank=True)
    question_3_subquestion_4 = models.CharField("Guiding improvements",max_length=50,choices=guiding_choices, blank=True)
    

    date_published = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return("Questionnaire response "+str(self.pk))



# Create your models here.