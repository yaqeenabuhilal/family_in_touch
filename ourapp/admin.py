from django.contrib import admin
# # Register your models here.
# from .models import teengers
from .models import *
# from .models import Parents
from .models import profile

admin.site.register(Parents)
admin.site.register(Teengers)
admin.site.register(Psychotherapist)
admin.site.register(Lecture)
admin.site.register(ParentFeedback)
admin.site.register(TeengerFeedback)
admin.site.register(profile)
