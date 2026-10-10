import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='course_thumbnails/', blank=True, null=True)
    is_published = models.BooleanField(default=False)
    allow_jumping_ahead = models.BooleanField(
        default=False, 
        help_text="If false, students can only view unlocked lessons consecutively."
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Day(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='days')
    day_number = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=255)
    objectives = models.TextField(help_text="Line-separated list or summary of objectives")
    content = models.TextField(help_text="Rich explanatory content or Markdown/HTML")
    code_snippet = models.TextField(blank=True, help_text="Sample code demonstration")
    practice_tasks = models.TextField(blank=True, help_text="Hands-on practice exercises")
    video_url = models.URLField(blank=True, help_text="YouTube or external embed URL")
    file = models.FileField(upload_to='course_files/', blank=True, null=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        unique_together = ('course', 'day_number')
        ordering = ['day_number']

    def __str__(self):
        return f"{self.course.title} - Day {self.day_number}: {self.title}"


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.title}"


class LessonProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='user_progress')
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'day')

    def __str__(self):
        return f"{self.user.username} - Day {self.day.day_number} ({'Done' if self.is_completed else 'Pending'})"


class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificates')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='certificates')
    certificate_code = models.CharField(max_length=50, unique=True, blank=True, editable=False)
    issued_at = models.DateTimeField(auto_now_add=True)
    certificate_image = models.ImageField(upload_to='certificates/', blank=True, null=True)

    class Meta:
        unique_together = ('user', 'course')

    def save(self, *args, **kwargs):
        if not self.certificate_code:
            self.certificate_code = f"CERT-{uuid.uuid4().hex[:10].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Certificate: {self.user.username} - {self.course.title}"