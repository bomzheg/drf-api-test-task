from django.contrib import admin

from .models import Question, PossibleAnswer, Poll

admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(PossibleAnswer)
