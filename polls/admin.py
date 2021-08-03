from django.contrib import admin
from.models import *
admin.site.register(Question)
#
admin.site.register(Choice)
# Register your mode


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')