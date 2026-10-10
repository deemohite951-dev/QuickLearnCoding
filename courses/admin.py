from django.contrib import admin
from .models import Course, Day, Enrollment, LessonProgress, Certificate


class DayInline(admin.StackedInline):
    model = Day
    extra = 0
    fields = ('day_number', 'title', 'is_published')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'allow_jumping_ahead', 'created_at')
    list_filter = ('is_published', 'allow_jumping_ahead')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [DayInline]


@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('course', 'day_number', 'title', 'is_published')
    list_filter = ('course', 'is_published')
    search_fields = ('title', 'content', 'objectives')


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'enrolled_at')
    search_fields = ('user__username', 'course__title')


@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'day', 'is_completed', 'completed_at')
    list_filter = ('is_completed', 'day__course')
    search_fields = ('user__username', 'day__title')
    actions = ['reset_progress']

    @admin.action(description="Reset selected users' lesson progress")
    def reset_progress(self, request, queryset):
        queryset.update(is_completed=False, completed_at=None)
        self.message_user(request, "Selected progress records have been reset.")


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'certificate_code', 'issued_at')
    search_fields = ('user__username', 'course__title', 'certificate_code')
    readonly_fields = ('certificate_code', 'issued_at')