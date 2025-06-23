from django.db import models

class Participant(models.Model):
    name = models.CharField(max_length=100)
    token_number = models.PositiveIntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=False, default='')  
    home_parish = models.CharField(max_length=100,default='')
  # not required at form level
    is_winner = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} (Token #{self.token_number})"
