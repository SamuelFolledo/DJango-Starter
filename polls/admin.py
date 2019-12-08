from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline): #StackedInLine will have it stack, TabularInLine is cleaner
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline] #puts it in the same field
    list_display = ('question_text', 'pub_date', 'was_published_recently') #displays these properties on showing lists of polls
    list_filter = ['pub_date'] #filter!!!!
    search_fields = ['question_text'] #search question text

admin.site.register(Question, QuestionAdmin)

# admin.site.register(Choice) #will create another thing, but if we want it in the same line (if they are related)
# then we will want an StackedInLine
