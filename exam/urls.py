
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # Home
    path('', views.home, name='home'),

    # Authentication
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
path(
    'password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
    name='password_reset'
),

path(
    'password-reset/done/',
    auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ),
    name='password_reset_done'
),

path(
    'reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'
    ),
    name='password_reset_confirm'
),

path(
    'reset/done/',
    auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'
    ),
    name='password_reset_complete'
),
    # Dashboards
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),

    # Subject
    path('create-subject/', views.create_subject, name='create_subject'),

    # Exam
    path('create-exam/', views.create_exam, name='create_exam'),
    path('my-exams/', views.my_exams, name='my_exams'),
    path('student-exams/', views.student_exams, name='student_exams'),

    # MCQ Question
    path(
        'add-question/<int:exam_id>/',
        views.add_question,
        name='add_question'
    ),

    # Coding Question
    path('add-coding-question/<int:exam_id>/', views.add_coding_question, name='add_coding_question'),

    # Exam
    path(
        'start-exam/<int:exam_id>/',
        views.start_exam,
        name='start_exam'
    ),

    path(
        'submit-exam/<int:exam_id>/',
        views.submit_exam,
        name='submit_exam'
    ),

    path('coding-submissions/', views.coding_submissions, name='coding_submissions'),
    path('give-marks/<int:submission_id>/', views.give_marks, name='give_marks'),

    # Teacher Results
    path(
        'teacher-results/',
        views.view_results,
        name='teacher_results'
    ),

    # Student Results
    path(
        'my-results/',
        views.student_results,
        name='student_results'
    ),

    # Leaderboard
    path(
        'leaderboard/',
        views.leaderboard,
        name='leaderboard'
    ),

    # Edit Exam
    path(
        'edit-exam/<int:exam_id>/',
        views.edit_exam,
        name='edit_exam'
    ),

    path(
        'delete-exam/<int:exam_id>/',
        views.delete_exam,
        name='delete_exam'
    ),

    path(
        'publish-exam/<int:exam_id>/',
        views.publish_exam,
        name='publish_exam'
    ),

    # Coding Submissions
    path(
        'coding-submissions/',
        views.coding_submissions,
        name='coding_submissions'
    ),

    path(
        'give-marks/<int:submission_id>/',
        views.give_marks,
        name='give_marks'
    ),

    # PDF Download
    path(
        'download-result/<int:result_id>/',
        views.download_result_pdf,
        name='download_result'
    ),

    path(
    'view-mcq/<int:exam_id>/',
    views.view_mcq,
    name='view_mcq_questions'
),
    path(
    'view-coding/<int:exam_id>/',
    views.view_coding,
    name='view_coding_questions'
),
]

