from django.db import models
from django.contrib.auth.models import AbstractUser

# User = get_user_model()  not recommended

class User(AbstractUser):
    pass  # no need to more than exist in AbstractUser class

class Lead(models.Model):
    SOURCE_CHOICES = (
        ("YouTube", "YouTube"),
        ("Google", "Google"),
        ("Newsletter", "Newsletter"),
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=100)
    profile_picture = models.ImageField(blank=True, null=True)
    special_file = models.FileField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Agent(models.Model):
    user : User = models.OneToOneField("User", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.email