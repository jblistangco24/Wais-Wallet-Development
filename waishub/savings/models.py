from django.db import models

class Saving(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, blank=True)
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    goal_term = models.CharField(max_length=100, blank=True)  # e.g., '6 months'
    reminder_frequency = models.CharField(max_length=100, blank=True)  # e.g., 'weekly'

    def __str__(self):
        return f"{self.date} - {self.category}: ₱{self.amount}"
