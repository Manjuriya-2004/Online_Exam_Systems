from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Subject)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(CodingQuestion)
admin.site.register(CodingSubmission)
admin.site.register(Result)