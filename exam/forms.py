# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import (
#     CustomUser,
#     Subject,
#     Exam,
#     Question,
#     CodingQuestion,
#     Task,
#     TaskSubmission
# )


# # Register Form
# class RegisterForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'role', 'password1', 'password2']


# # Subject Form
# class SubjectForm(forms.ModelForm):
#     class Meta:
#         model = Subject
#         fields = ['name']


# # Exam Form
# class ExamForm(forms.ModelForm):
#     class Meta:
#         model = Exam
#         exclude = ['created_by']
#         widgets = {
#             'subject': forms.Select(attrs={'class': 'form-select'}),
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'duration': forms.NumberInput(attrs={'class': 'form-control'}),
#             'total_marks': forms.NumberInput(attrs={'class': 'form-control'}),
#             'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
#         }


# # MCQ Question Form
# class QuestionForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = '__all__'
#         widgets = {
#             'question_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
#             'option_a': forms.TextInput(attrs={'class': 'form-control'}),
#             'option_b': forms.TextInput(attrs={'class': 'form-control'}),
#             'option_c': forms.TextInput(attrs={'class': 'form-control'}),
#             'option_d': forms.TextInput(attrs={'class': 'form-control'}),
#             'correct_option': forms.Select(attrs={'class': 'form-select'}),
#         }


# # Coding Question Form
# class CodingQuestionForm(forms.ModelForm):
#     class Meta:
#         model = CodingQuestion
#         fields = '__all__'
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'problem_statement': forms.Textarea(attrs={'class': 'form-control'}),
#             'sample_input': forms.Textarea(attrs={'class': 'form-control'}),
#             'sample_output': forms.Textarea(attrs={'class': 'form-control'}),
#             'marks': forms.NumberInput(attrs={'class': 'form-control'}),
#         }


# # Task Form
# # Task Form
# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         exclude = ['exam']

#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'description': forms.Textarea(attrs={'class': 'form-control'}),
#             'marks': forms.NumberInput(attrs={'class': 'form-control'}),
#             'deadline': forms.DateTimeInput(
#                 attrs={
#                     'class': 'form-control',
#                     'type': 'datetime-local'
#                 }
#             ),
#         }


# # Task Submission Form
# class TaskSubmissionForm(forms.ModelForm):
#     class Meta:
#         model = TaskSubmission
#         fields = ['answer', 'file']
#         widgets = {
#             'answer': forms.Textarea(
#                 attrs={
#                     'class': 'form-control',
#                     'rows': 5
#                 }
#             )
#         }



from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import (
    CustomUser,
    Subject,
    Exam,
    Question,
    CodingQuestion
)


# =========================
# Register Form
# =========================

class RegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'role',
            'password1',
            'password2'
        ]


# =========================
# Subject Form
# =========================

class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ['name']


# =========================
# Exam Form
# =========================

class ExamForm(forms.ModelForm):

    class Meta:
        model = Exam
        exclude = ['created_by']

        widgets = {
            'subject': forms.Select(
                attrs={'class': 'form-select'}
            ),

            'title': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'duration': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),

            'total_marks': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),

            'is_published': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
            ),
        }


# =========================
# MCQ Question Form
# =========================

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = '__all__'

        widgets = {
            'question_text': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3
                }
            ),

            'option_a': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'option_b': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'option_c': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'option_d': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'correct_option': forms.Select(
                attrs={'class': 'form-select'}
            ),
        }


# =========================
# Coding Question Form
# =========================

class CodingQuestionForm(forms.ModelForm):
    class Meta:
        model = CodingQuestion
        fields = [
    'title',
    'problem_statement',
    'sample_input',
    'sample_output',
    'marks'
]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'problem_statement': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10
            }),

            'sample_input': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),

            'sample_output': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),

            'marks': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
        }

