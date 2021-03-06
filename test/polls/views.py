from django.http import Http404
from django.shortcuts import render
from django.http import  HttpResponse
from .models import Question
# Create your views here.
def index(request):
    return HttpResponse("hello world this is polls home")
def detail(request,question_id):
    return HttpResponse("You're looking at question %s" % question_id)
def results(request,question_id):
    response ="You're looking at the results of question %s"
    return HttpResponse(response % question_id)
def vote(request,question_id):
    return HttpResponse("You're voting on question %s" % question_id)
def error(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Questin does not exist")
    return request
    latest_question_list = Question.objects.order_by('-pub_date')[:1]
    context = {
        'latest_question_list':latest_question_list
    }
    return render(request,'index.html',context)