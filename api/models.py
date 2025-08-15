from django.db import models
from django.contrib.auth.models import User

class report(models.Model):
  full_name = models.CharField(max_length=100)
  gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
  location = models.CharField(max_length=100)
  condition = models.TextField()
  date = models.DateField(auto_now_add=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')

  def __str__(self):
    return self.full_name