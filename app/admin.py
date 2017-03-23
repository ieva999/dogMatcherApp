from django.contrib import admin
from app.models import UserProfile, Dog, MatchingMetric

admin.site.register(UserProfile)
admin.site.register(Dog)
admin.site.register(MatchingMetric)
