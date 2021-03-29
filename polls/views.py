from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Choice, Question

# Create your views here.


#def index (request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {
#        'latest_question_list':latest_question_list,
#    }
#    return render(request,'polls/index.html',context)
#    #template = loader.get_template('polls/index.html')
#    #return HttpResponse(template.render(context,request))
#    #output = ','.join([q.question_text for q in latest_question_list]) #这个写法还是挺方便的
#    #return HttpResponse(output) 
#    # return HttpResponse("hello again ,the pills index.")

#def detail(request,question_id):
#    question = get_object_or_404(Question,pk = question_id)
#    return render(request,'polls/detail.html',{'question':question})
#    #try:
#    #    question = Question.objects.get(pk = question_id)
#    #except Question.DoesNotExist:
#    #    raise Http404("Question does not exist")
#    #return render(request,"polls/detail.html",{'question':question})
#    #return HttpResponse("You're looking at question %s" % question_id)

#def results(request,question_id):
#    question = get_object_or_404(Question,pk=question_id)
#    return render(request,'polls/results.html',{'question':question})
#    #response = "You're looking at the results of question %s"
#    #return HttpResponse(response % question_id)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    # 为了防止用户盲猜url，访问到我们你现在还不打算让他们看到的页面，添加约束
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte = timezone.now())
        

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request,question_id):
    question = get_object_or_404(Question,pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
    # return HttpResponse( "You're voting on question %s" % question_id)
