from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Quiz, Option, QuizAttempt

@login_required
def quiz_detail_view(request, quiz_id):
    quiz = get_object_or_404(Quiz.objects.prefetch_related('questions__options'), id=quiz_id)

    if request.method == 'POST':
        questions = quiz.questions.all()
        total_questions = questions.count()
        if total_questions == 0:
            messages.warning(request, "This quiz has no questions.")
            return redirect('courses:day_detail', slug=quiz.day.course.slug, day_number=quiz.day.day_number)

        correct_count = 0
        breakdown = []

        for q in questions:
            selected_option_id = request.POST.get(f"question_{q.id}")
            selected_option = None
            is_correct = False

            if selected_option_id:
                try:
                    selected_option = Option.objects.get(id=int(selected_option_id), question=q)
                    if selected_option.is_correct:
                        is_correct = True
                        correct_count += 1
                except (Option.DoesNotExist, ValueError):
                    pass

            correct_option = q.options.filter(is_correct=True).first()

            breakdown.append({
                'question': q.question_text,
                'selected': selected_option.option_text if selected_option else "No answer selected",
                'correct_answer': correct_option.option_text if correct_option else "N/A",
                'is_correct': is_correct,
                'explanation': q.explanation
            })

        score_percent = round((correct_count / total_questions) * 100, 2)
        passed = score_percent >= quiz.passing_score

        # Save Attempt
        QuizAttempt.objects.create(
            user=request.user,
            quiz=quiz,
            score=score_percent
        )

        return render(request, 'quizzes/quiz_result.html', {
            'quiz': quiz,
            'score': score_percent,
            'passed': passed,
            'correct_count': correct_count,
            'total_questions': total_questions,
            'breakdown': breakdown,
            'day': quiz.day
        })

    return render(request, 'quizzes/quiz_detail.html', {'quiz': quiz})