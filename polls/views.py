from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader #needed for templating
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5] #grab 5 most recent questions 
    # output = ', '.join([q.question_text for q in latest_question_list]) #get each Question's text contained in a string and separated by a comma
    # return HttpResponse(output) # Leave the rest of the views (detail, results, vote) unchanged
    template = loader.get_template('polls/index.html') #subdirectory polls inside our polls app; loads the template and passes it a context dictionary
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)