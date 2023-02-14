from django.db import models


class Word(models.Model):

    id = models.AutoField(primary_key=True)
    first_word = models.CharField(max_length=255)
    second_word = models.CharField(max_length=255)

   
    
    
    