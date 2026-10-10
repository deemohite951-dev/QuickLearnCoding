from django.urls import path
from .views import (
    course_list_view,
    course_detail_view,
    enroll_course_view,
    dashboard_view,
    day_detail_view,
    mark_lesson_complete_view,
    view_certificate_view
)

app_name = 'courses'

urlpatterns = [
    path('', course_list_view, name='course_list'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('<slug:slug>/', course_detail_view, name='course_detail'),
    path('<slug:slug>/enroll/', enroll_course_view, name='enroll'),
    path('<slug:slug>/day/<int:day_number>/', day_detail_view, name='day_detail'),
    path('<slug:slug>/day/<int:day_number>/complete/', mark_lesson_complete_view, name='mark_complete'),
    path('certificate/<str:code>/', view_certificate_view, name='view_certificate'),
]