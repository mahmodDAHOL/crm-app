from django.contrib import admin
from .models import Category, FollowUp, User, Lead, Agent, UserProfile

admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Agent)
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(FollowUp)