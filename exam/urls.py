from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('create-subject/', views.create_subject, name='create_subject'),
    path('create-exam/', views.create_exam, name='create_exam'),
    #path('add-question/', views.add_question, name='add_question'),
    path('add-question/<int:exam_id>/', views.add_question, name='add_question'),
    path('start-exam/<int:exam_id>/', views.start_exam, name='start_exam'),
    path('submit-exam/<int:exam_id>/', views.submit_exam, name='submit_exam'),
    path('teacher-results/', views.view_results, name='teacher_results'),
    #path('download-result/<int:exam_id>/', views.download_result_pdf, name='download_result_pdf'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('my-exams/', views.my_exams, name='my_exams'),
    path('student-exams/', views.student_exams, name='student_exams'),
    path('edit-exam/<int:exam_id>/', views.edit_exam, name='edit_exam'),
    path('delete-exam/<int:exam_id>/', views.delete_exam, name='delete_exam'),
    path('publish-exam/<int:exam_id>/', views.publish_exam, name='publish_exam'),
    path('my-results/', views.student_results, name='student_results'),
    path('download-result/<int:result_id>/', views.download_result_pdf, name='download_result'),

]