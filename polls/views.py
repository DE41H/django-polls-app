from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'index.html', context)

def detail(request, question_id):
    return HttpResponse()

def results(request, question_id):
    return HttpResponse()

def vote(request, question_id):
    return HttpResponse()
