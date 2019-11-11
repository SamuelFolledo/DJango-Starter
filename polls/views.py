from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect #Part4 - HttpResponseRedirect takes a single argument: the URL to which the user will be redirected
from django.urls import reverse

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5] #grab 5 most recent questions 
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context) #django.shortcut render
    
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) #django.shortcut to get if the question exist or not
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id): #part 4
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        context = {
            'question': question,
            'error_message': "You didn't select a choice.",
        }
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))