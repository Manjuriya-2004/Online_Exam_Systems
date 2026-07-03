# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.conf import settings


# # =========================
# # Users
# # =========================

# class CustomUser(AbstractUser):

#     ROLE_CHOICES = (
#         ('admin', 'Admin'),
#         ('teacher', 'Teacher'),
#         ('student', 'Student'),
#     )

#     role = models.CharField(max_length=10, choices=ROLE_CHOICES)

#     def __str__(self):
#         return self.username


# # =========================
# # Subject
# # =========================

# class Subject(models.Model):
#     name = models.CharField(max_length=100)

#     created_by = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE
#     )

#     def __str__(self):
#         return self.name


# # =========================
# # Exam
# # =========================

# class Exam(models.Model):
#     subject = models.ForeignKey(
#         Subject,
#         on_delete=models.CASCADE
#     )

#     title = models.CharField(max_length=200)

#     duration = models.IntegerField(
#         help_text="Duration in minutes"
#     )

#     total_marks = models.IntegerField()

#     created_by = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         limit_choices_to={'role': 'teacher'}
#     )

#     is_published = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title


# # =========================
# # MCQ Questions
# # =========================

# class Question(models.Model):
#     exam = models.ForeignKey(
#         Exam,
#         on_delete=models.CASCADE,
#         related_name='questions'
#     )

#     question_text = models.TextField()

#     option_a = models.CharField(max_length=200)
#     option_b = models.CharField(max_length=200)
#     option_c = models.CharField(max_length=200)
#     option_d = models.CharField(max_length=200)

#     CORRECT_CHOICES = (
#         ('A', 'Option A'),
#         ('B', 'Option B'),
#         ('C', 'Option C'),
#         ('D', 'Option D'),
#     )

#     correct_option = models.CharField(
#         max_length=1,
#         choices=CORRECT_CHOICES
#     )

#     def __str__(self):
#         return self.question_text


# # =========================
# # Coding Questions
# # =========================

# class CodingQuestion(models.Model):

#     exam = models.ForeignKey(
#         Exam,
#         on_delete=models.CASCADE,
#         related_name='coding_questions'
#     )

#     title = models.CharField(max_length=200)

#     problem_statement = models.TextField()

#     sample_input = models.TextField()

#     sample_output = models.TextField()

#     marks = models.IntegerField(default=10)

#     def __str__(self):
#         return self.title


# # =========================
# # Coding Submission
# # =========================

# class CodingSubmission(models.Model):

#     student = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         limit_choices_to={'role': 'student'}
#     )

#     coding_question = models.ForeignKey(
#         CodingQuestion,
#         on_delete=models.CASCADE
#     )

#     code = models.TextField()

#     language = models.CharField(
#         max_length=20,
#         default='Python'
#     )

#     score = models.IntegerField(default=0)

#     submitted_at = models.DateTimeField(
#         auto_now_add=True
#     )

#     def __str__(self):
#         return f"{self.student.username} - {self.coding_question.title}"


# # =========================
# # Assignment / Task
# # =========================

# class Task(models.Model):

#     exam = models.ForeignKey(
#         Exam,
#         on_delete=models.CASCADE,
#         related_name='tasks'
#     )

#     title = models.CharField(max_length=200)

#     description = models.TextField()

#     marks = models.IntegerField(default=10)

#     deadline = models.DateTimeField()

#     def __str__(self):
#         return self.title


# # =========================
# # Task Submission
# # =========================

# class TaskSubmission(models.Model):

#     task = models.ForeignKey(
#         Task,
#         on_delete=models.CASCADE,
#         related_name='submissions'
#     )

#     student = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         limit_choices_to={'role': 'student'}
#     )

#     answer = models.TextField(blank=True)

#     file = models.FileField(
#         upload_to='task_submissions/',
#         blank=True,
#         null=True
#     )

#     score = models.IntegerField(default=0)

#     submitted_at = models.DateTimeField(
#         auto_now_add=True
#     )

#     def __str__(self):
#         return f"{self.student.username} - {self.task.title}"


# # =========================
# # Result
# # =========================

# class Result(models.Model):

#     student = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         limit_choices_to={'role': 'student'}
#     )

#     exam = models.ForeignKey(
#         Exam,
#         on_delete=models.CASCADE
#     )

#     score = models.IntegerField()

#     percentage = models.FloatField()

#     date = models.DateTimeField(
#         auto_now_add=True
#     )

#     def __str__(self):
#         return f"{self.student.username} - {self.exam.title}"
    
# class CodingQuestions(models.Model):
#     exam = models.ForeignKey(
#         Exam,
#         on_delete=models.CASCADE,
#         related_name='coding_questions'
#     )

#     title = models.CharField(max_length=200)

#     problem_statement = models.TextField()

#     marks = models.IntegerField(default=10)



from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


# =========================
# Users
# =========================

class CustomUser(AbstractUser):

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username


# =========================
# Subject
# =========================

class Subject(models.Model):

    name = models.CharField(max_length=100)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


# =========================
# Exam
# =========================

class Exam(models.Model):

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)

    duration = models.IntegerField(
        help_text="Duration in minutes"
    )

    total_marks = models.IntegerField()

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'teacher'}
    )

    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# =========================
# MCQ Questions
# =========================

class Question(models.Model):

    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name='questions'
    )

    question_text = models.TextField()

    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)

    CORRECT_CHOICES = (
        ('A', 'Option A'),
        ('B', 'Option B'),
        ('C', 'Option C'),
        ('D', 'Option D'),
    )

    correct_option = models.CharField(
        max_length=1,
        choices=CORRECT_CHOICES
    )

    def __str__(self):
        return self.question_text


# =========================
# Coding Questions
# =========================

class CodingQuestion(models.Model):

    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name='coding_questions'
    )

    title = models.CharField(max_length=200)

    problem_statement = models.TextField()

    sample_input = models.TextField(
        blank=True,
        null=True
    )

    sample_output = models.TextField(
        blank=True,
        null=True
    )

    marks = models.IntegerField(default=10)

    def __str__(self):
        return self.title


# =========================
# Coding Submission
# =========================

class CodingSubmission(models.Model):

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'student'}
    )

    coding_question = models.ForeignKey(
        CodingQuestion,
        on_delete=models.CASCADE
    )

    code = models.TextField()

    language = models.CharField(
        max_length=20,
        default='Python'
    )

    score = models.IntegerField(default=0)

    submitted_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.student.username} - {self.coding_question.title}"


# =========================
# Result
# =========================

class Result(models.Model):

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'student'}
    )

    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE
    )

    score = models.IntegerField()

    percentage = models.FloatField()

    date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.student.username} - {self.exam.title}"


class ExamAttempt(models.Model):
    student = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE
)
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
    end_time = models.DateTimeField()