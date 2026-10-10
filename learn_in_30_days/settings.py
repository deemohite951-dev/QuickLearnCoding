import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
load_dotenv(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = os.getenv('SECRET_KEY', 'default-unsecure-key-change-in-production')
DEBUG = os.getenv('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = [host.strip() for host in os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')]

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Custom local apps
    'core.apps.CoreConfig',
    'accounts.apps.AccountsConfig',
    'courses.apps.CoursesConfig',
    'quizzes.apps.QuizzesConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'learn_in_30_days.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'learn_in_30_days.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': {'min_length': 6}},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'courses:dashboard'
LOGOUT_REDIRECT_URL = 'core:home'
LOGIN_URL = 'accounts:login'

JAZZMIN_SETTINGS = {
    # Title & branding
    'site_title': 'Learn in 30 Days Admin',
    'site_header': 'Learn in 30 Days',
    'site_brand': 'Learn in 30 Days',
    'welcome_sign': 'Welcome to the Course & Content Manager',
    'copyright': 'Learn in 30 Days Ltd',
    'search_model': ['auth.User', 'courses.Course', 'courses.Day'],
    # Navigation bar
    'topmenu_links': [
        {'name': 'Home', 'url': 'admin:index', 'permissions': ['auth.view_user']},
        {'name': 'View Site', 'url': '/'},
    ],
    # App & model icons (FontAwesome Free icons)
    'icons': {
        'auth': 'fas fa-users-cog',
        'auth.user': 'fas fa-user',
        'auth.Group': 'fas fa-users',
        'accounts.Profile': 'fas fa-id-card',
        'courses.Course': 'fas fa-graduation-cap',
        'courses.Day': 'fas fa-calendar-day',
        'courses.Enrollment': 'fas fa-user-graduate',
        'courses.LessonProgress': 'fas fa-tasks',
        'quizzes.Quiz': 'fas fa-question-circle',
        'quizzes.Question': 'fas fa-list-ol',
        'quizzes.QuizAttempt': 'fas fa-poll',
    },
    'default_icon_parents': 'fas fa-chevron-circle-right',
    'default_icon_children': 'fas fa-circle',
    'show_sidebar': True,
    'navigation_expanded': True,
    'changeform_format': 'horizontal_tabs',
}

JAZZMIN_UI_TWEAKS = {
    'theme': 'flatly',  # Clean modern theme: flatly, darkly, pulse, etc.
    'dark_mode_theme': None,
    'navbar': 'navbar-dark bg-primary',
    'sidebar': 'sidebar-dark-primary',
    'brand_small_text': False,
    'accent': 'accent-primary',
}