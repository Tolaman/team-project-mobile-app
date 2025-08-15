from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
  full_name = models.CharField(max_length=100)
  gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
  location = models.CharField(max_length=100)
  condition = models.TextField()
  date = models.DateField(auto_now_add=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')

  def __str__(self):
    return self.full_name
  
class Shelter(models.Model):
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=255)
  phone_number = models.CharField(max_length=15)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name