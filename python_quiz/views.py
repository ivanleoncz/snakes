from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Question, Answer

def index(request):
    return render(request, "python_quiz/index.html")


def questions(request):
    context = {
            "questions": Question.objects.all()
    }
    return render(request, "python_quiz/questions.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'python_quiz/detail.html', {'question': question})
