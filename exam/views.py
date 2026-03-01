from django.shortcuts import render , redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm,QuestionForm,SubjectForm, ExamForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Subject, Exam, Question,Result
from django.http import HttpResponseForbidden
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.db.models import Avg, Count, Q, F , Count , Sum
#from django.db.models import Count
from django.utils import timezone
import json
from django.contrib import messages
#from django.contrib.auth.decorators import login_required
#from django.db.models import Count
#from .models import Exam, Question
from django.core.mail import send_mail
from django.conf import settings

#...Home...#

def home(request):
    return render(request, 'home.html')

#....Register....#

def register_view(request):
    form = RegisterForm()
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    return render(request, 'register.html', {'form': form})


#....Login....#

def login_view(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'teacher':
                return redirect('teacher_dashboard')
            else:
                return redirect('student_dashboard')

        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')



#....logout....#

def logout_view(request):
    logout(request)
    return redirect('login')


#....Dashboard...#

@login_required    #admin dashboard
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required  #teacher dashboard
def teacher_dashboard(request):

    exams = Exam.objects.filter(created_by=request.user)
    total_exams = exams.count()
    published_exams = exams.filter(is_published=True).count()
    total_questions = Question.objects.filter(exam__created_by=request.user).count()

    # Chart Data
    exam_titles = []
    question_counts = []

    for exam in exams:
        exam_titles.append(exam.title)
        question_counts.append(
            Question.objects.filter(exam=exam).count()
        )

    return render(request, 'teacher_dashboard.html', {
    'total_exams': total_exams,
    'published_exams': published_exams,
    'total_questions': total_questions,
    'exam_titles': json.dumps(exam_titles),
    'question_counts': json.dumps(question_counts),
    })

@login_required  #student dashboard
def student_dashboard(request):

    results = Result.objects.filter(student=request.user)
    total_exams = results.count()
    passed = results.filter(score__gte=50).count()
    failed = results.filter(score__lt=50).count()

    return render(request, 'student_dashboard.html', {
        'total_exams': total_exams,
        'passed': passed,
        'failed': failed,
        'chart_data': json.dumps([passed, failed]),
    })


#...Teacher...#

@login_required  #create subject
def create_subject(request):
    if request.user.role != 'teacher':
        return HttpResponseForbidden("Not Allowed")

    form = SubjectForm()
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.created_by = request.user
            subject.save()
            return redirect('teacher_dashboard')

    return render(request, 'create_subject.html', {'form': form})


@login_required  #create exam
def create_exam(request):
    if request.user.role != 'teacher':
        return HttpResponseForbidden("Not Allowed")

    form = ExamForm()
    if request.method == "POST":
        form = ExamForm(request.POST)
        if form.is_valid():
            exam = form.save(commit=False)
            exam.created_by = request.user
            exam.save()
            return redirect('teacher_dashboard')

    return render(request, 'create_exam.html', {'form': form})


#...Add questions...#

@login_required    #add question
def add_question(request, exam_id):

    if request.user.role != 'teacher':
        return HttpResponseForbidden("Not Allowed")

    exam = Exam.objects.get(id=exam_id)

    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.exam = exam   # 🔥 link question to that exam
            question.save()
            return redirect('my_exams')
    else:
        form = QuestionForm()

    return render(request, 'add_question.html', {
        'form': form,
        'exam': exam
    })



#...start exam...#


@login_required  #start exam
def start_exam(request, exam_id):

    if request.user.role != 'student':
        return HttpResponseForbidden("Not Allowed")

    # safer query (also ensure published only)
    exam = get_object_or_404(Exam, id=exam_id, is_published=True)

    # 🔥 SCHEDULING CHECK END
    questions = Question.objects.filter(exam=exam)

    return render(request, 'exam_page.html', {
        'exam': exam,
        'questions': questions,
        'duration': exam.duration
    })


#...submit...#

@login_required   #submit exam
def submit_exam(request, exam_id):

    if request.user.role != 'student':
        return HttpResponseForbidden("Not Allowed")

    exam = Exam.objects.get(id=exam_id)
    questions = Question.objects.filter(exam=exam)
    # Prevent duplicate attempt
    if Result.objects.filter(student=request.user, exam=exam).exists():
        return HttpResponseForbidden("You already attempted this exam.")
    score = 0
    for question in questions:
        selected = request.POST.get(str(question.id))
        if selected == question.correct_option:
            score += 1

    total = questions.count()
    percentage = (score / total) * 100 if total > 0 else 0

    #  Save result and store object
    result = Result.objects.create(
        student=request.user,
        exam=exam,
        score=score,
        percentage=percentage
    )

    subject = f"Exam Result - {exam.title}"
    status = "PASSED" if percentage >= 50 else "FAILED"

    message = f"""
Hello {request.user.username},

You have completed the exam: {exam.title}

Score: {score}/{total}
Percentage: {percentage:.2f}%
Status: {status}

Thank you.
"""

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [request.user.email],
        fail_silently=False,
    )

    return render(request, 'result.html', {
        'score': score,
        'total': total,
        'percentage': percentage,
        'result': result   
    })


#Result...#

@login_required   # View results-teacher
def view_results(request):
    if request.user.role != 'teacher':
        return HttpResponseForbidden("Not Allowed")

    results = Result.objects.filter(
        exam__created_by=request.user
    )

    return render(request, 'teacher_results.html', {
        'results': results
    })


#...PDF generate...#
"""@login_required
def download_result_pdf(request, result_id):
    result = Result.objects.get(id=result_id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="result_{result.id}.pdf"'
    p = canvas.Canvas(response)
    p.drawString(100, 800, "Exam Result")
    p.drawString(100, 770, f"Student: {result.student.username}")
    p.drawString(100, 750, f"Exam: {result.exam.title}")
    p.drawString(100, 730, f"Score: {result.score}")
    p.drawString(100, 710, f"Percentage: {result.percentage}%")
    p.showPage()
    p.save()
    return response"""
"""#...Leaderboard...#
@login_required
def leaderboard(request):
    results = Result.objects.all().order_by('-percentage')
    return render(request, 'leaderboard.html', {
        'results': results
    })
"""

# my exams -teacher
@login_required
def my_exams(request):
    exams = Exam.objects.filter(created_by=request.user) \
                        .annotate(question_count=Count('questions'))

    return render(request, 'my_exams.html', {
        'exams': exams
    })


#student exam
@login_required
def student_exams(request): # exams-student

    if request.user.role != 'student':
        return HttpResponseForbidden("Not Allowed")

    subjects = Subject.objects.all()
    subject_id = request.GET.get('subject')

    exams = None
    attempted_exam_ids = []

    if subject_id:
        exams = Exam.objects.filter(subject_id=subject_id,is_published=True)

        attempted_exam_ids = Result.objects.filter(
            student=request.user
        ).values_list('exam_id', flat=True)

    return render(request, 'student_exams.html', {
        'subjects': subjects,
        'exams': exams,
        'attempted_exam_ids': attempted_exam_ids,
        'now': timezone.now()
    })



#edit exam
@login_required  #edit exam-teacher
def edit_exam(request, exam_id):
    if request.user.role != 'teacher':
        return HttpResponseForbidden("Not Allowed")
    exam = get_object_or_404(Exam, id=exam_id, created_by=request.user)
    if request.method == "POST":
        form = ExamForm(request.POST, instance=exam)
        if form.is_valid():
            form.save()
            return redirect('my_exams')
    else:
        form = ExamForm(instance=exam)

    return render(request, 'edit_exam.html', {'form': form})


@login_required   #delete exam-teacher
def delete_exam(request, exam_id):
    if request.user.role != 'teacher':
        return HttpResponseForbidden("Not Allowed")
    exam = get_object_or_404(Exam, id=exam_id, created_by=request.user)
    exam.delete()
    return redirect('my_exams')

#Publish exam

@login_required  #pulish exam-teacher
def publish_exam(request, exam_id):
    if request.user.role != 'teacher':
        return HttpResponseForbidden("Not Allowed")
    exam = get_object_or_404(
        Exam,
        id=exam_id,
        created_by=request.user
    )
    exam.is_published = True
    exam.save()
    return redirect('my_exams')


#student results
@login_required
def student_results(request):  # Student-Results
    if request.user.role != 'student':
        return HttpResponseForbidden("Not Allowed")
    results = Result.objects.filter(student=request.user)
    return render(request, 'student_results.html', {
        'results': results
    })


#leader board
@login_required
def leaderboard(request):
    leaderboard_data = (
        Result.objects
        .values('student__username')
        .annotate(total_score=Sum('score'))
        .order_by('-total_score')
    )
    # Add rank manually
    ranked_list = []
    rank = 1
    for entry in leaderboard_data:
        ranked_list.append({
            'rank': rank,
            'username': entry['student__username'],
            'total_score': entry['total_score']
        })
        rank += 1

    return render(request, 'leaderboard.html', {
        'leaderboard': ranked_list
    })

#Download PDF 

@login_required
def download_result_pdf(request, result_id):

    result = Result.objects.get(id=result_id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="result_{result.id}.pdf"'

    p = canvas.Canvas(response)

    p.drawString(100, 800, "Exam Result")
    p.drawString(100, 770, f"Student: {result.student.username}")
    p.drawString(100, 750, f"Exam: {result.exam.title}")
    p.drawString(100, 730, f"Score: {result.score}")
    p.drawString(100, 710, f"Percentage: {result.percentage}%")

    p.showPage()
    p.save()

    return response