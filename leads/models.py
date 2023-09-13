from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
# User = get_user_model()  not recommended

class User(AbstractUser):
    # when user sign up, he will be organizer then he can create agents, every agent can login afterward
    is_organizer = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)
    
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Lead(models.Model):
    SOURCE_CHOICES = (
        ("YouTube", "YouTube"),
        ("Google", "Google"),
        ("Newsletter", "Newsletter"),
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    agent = models.ForeignKey("Agent",null=True, blank=True, on_delete=models.SET_NULL)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=100)
    profile_picture = models.ImageField(blank=True, null=True)
    special_file = models.FileField(blank=True, null=True)
    category = models.ForeignKey("Category",null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Agent(models.Model):
    user : User = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.email


class Category(models.Model):
    name = models.CharField(max_length=30)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# create a signal where whenever a User object created then the function post_user_created_signal excuted
post_save.connect(post_user_created_signal, sender=User) 