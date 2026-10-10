from django.contrib import admin
from .models import Quiz, Question, Option, QuizAttempt

class OptionInline(admin.TabularInline):
    model = Option
    extra = 4

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'day', 'passing_score')
    search_fields = ('title', 'day__title')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'quiz')
    inlines = [OptionInline]
    search_fields = ('question_text',)

@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'score', 'attempted_at')
    list_filter = ('quiz', 'attempted_at')
    search_fields = ('user__username', 'quiz__title')