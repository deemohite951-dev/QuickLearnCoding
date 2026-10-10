from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm, ProfileUpdateForm
from courses.models import Enrollment, LessonProgress

def register_view(request):
    if request.user.is_authenticated:
        return redirect('courses:dashboard')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Account created successfully! Please sign in.")
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('courses:dashboard')

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            ident = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']

            # Lookup by email if formatted as email, else username
            user_obj = None
            if '@' in ident:
                user_obj = User.objects.filter(email__iexact=ident).first()
                username = user_obj.username if user_obj else None
            else:
                username = ident

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                next_url = request.GET.get('next', 'courses:dashboard')
                return redirect(next_url)
            else:
                messages.error(request, "Invalid username/email or password.")
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('core:home')

@login_required
def profile_view(request):
    profile = request.user.profile
    enrollments = Enrollment.objects.filter(user=request.user).select_related('course')
    completed_days_count = LessonProgress.objects.filter(user=request.user, is_completed=True).count()

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect('accounts:profile')
    else:
        form = ProfileUpdateForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
        'enrollments': enrollments,
        'completed_days_count': completed_days_count,
    }
    return render(request, 'accounts/profile.html', context)