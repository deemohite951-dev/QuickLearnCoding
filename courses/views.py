from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Course, Day, Enrollment, LessonProgress
from quizzes.models import QuizAttempt

def course_list_view(request):
    courses = Course.objects.filter(is_published=True)
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail_view(request, slug):
    course = get_object_or_404(Course, slug=slug, is_published=True)
    days = course.days.filter(is_published=True).order_by('day_number')
    is_enrolled = False
    if request.user.is_authenticated:
        is_enrolled = Enrollment.objects.filter(user=request.user, course=course).exists()
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'days': days,
        'is_enrolled': is_enrolled
    })

@login_required
def enroll_course_view(request, slug):
    course = get_object_or_404(Course, slug=slug, is_published=True)
    enrollment, created = Enrollment.objects.get_or_create(user=request.user, course=course)
    # enrollment, created = Enrollment.objects.get_or_url = Enrollment.objects.get_or_create(user=request.user, course=course)
    if created:
        messages.success(request, f"Enrolled in {course.title}! Start Day 1 now.")
    return redirect('courses:day_detail', slug=course.slug, day_number=1)

@login_required
def dashboard_view(request):
    enrollments = Enrollment.objects.filter(user=request.user).select_related('course')
    dashboard_data = []

    for enr in enrollments:
        total_days = enr.course.days.filter(is_published=True).count()
        completed_days = LessonProgress.objects.filter(
            user=request.user,
            day__course=enr.course,
            is_completed=True
        ).count()
        percent = int((completed_days / total_days * 100)) if total_days > 0 else 0

        # Find next resume day
        completed_day_ids = LessonProgress.objects.filter(
            user=request.user,
            day__course=enr.course,
            is_completed=True
        ).values_list('day__day_number', flat=True)

        next_day = 1
        for d in range(1, total_days + 1):
            if d not in completed_day_ids:
                next_day = d
                break
        else:
            next_day = total_days  # All done

        dashboard_data.append({
            'course': enr.course,
            'total_days': total_days,
            'completed_days': completed_days,
            'percent': percent,
            'next_day': next_day,
            'is_finished': (completed_days == total_days and total_days > 0)
        })

    quiz_attempts = QuizAttempt.objects.filter(user=request.user).select_related('quiz', 'quiz__day')[:10]

    return render(request, 'courses/dashboard.html', {
        'dashboard_data': dashboard_data,
        'quiz_attempts': quiz_attempts,
    })

@login_required
def day_detail_view(request, slug, day_number):
    course = get_object_or_404(Course, slug=slug, is_published=True)
    day = get_object_or_404(Day, course=course, day_number=day_number, is_published=True)

    # Check enrollment
    is_enrolled = Enrollment.objects.filter(user=request.user, course=course).exists()
    if not is_enrolled:
        messages.warning(request, "Please enroll in this course first.")
        return redirect('courses:course_detail', slug=course.slug)

    # Progression Gate: ensure previous day is completed unless jumping is allowed or it's Day 1
    if not course.allow_jumping_ahead and day_number > 1:
        prev_day = Day.objects.filter(course=course, day_number=day_number - 1).first()
        if prev_day:
            is_prev_completed = LessonProgress.objects.filter(
                user=request.user, day=prev_day, is_completed=True
            ).exists()
            if not is_prev_completed:
                messages.warning(request, f"Please complete Day {prev_day.day_number} before advancing.")
                return redirect('courses:day_detail', slug=course.slug, day_number=prev_day.day_number)

    progress, _ = LessonProgress.objects.get_or_create(user=request.user, day=day)
    has_quiz = hasattr(day, 'quiz')

    prev_day_obj = Day.objects.filter(course=course, day_number=day_number - 1, is_published=True).first()
    next_day_obj = Day.objects.filter(course=course, day_number=day_number + 1, is_published=True).first()

    return render(request, 'courses/day_detail.html', {
        'course': course,
        'day': day,
        'progress': progress,
        'has_quiz': has_quiz,
        'prev_day': prev_day_obj,
        'next_day': next_day_obj,
    })

@login_required
def mark_lesson_complete_view(request, slug, day_number):
    if request.method == 'POST':
        course = get_object_or_404(Course, slug=slug)
        day = get_object_or_404(Day, course=course, day_number=day_number)
        progress, _ = LessonProgress.objects.get_or_create(user=request.user, day=day)
        progress.is_completed = True
        progress.completed_at = timezone.now()
        progress.save()
        messages.success(request, f"Day {day_number} marked as complete!")

        next_day = Day.objects.filter(course=course, day_number=day_number + 1, is_published=True).first()
        if next_day:
            return redirect('courses:day_detail', slug=course.slug, day_number=next_day.day_number)
        return redirect('courses:dashboard')

    return redirect('courses:day_detail', slug=slug, day_number=day_number)