from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Election, Candidate
# from .models import Choice, Question


def home_screen_view(request):
    # array, string or variable that can get referenced by html file
    context = {
        'test_string': "Working as intended",
    }
    return render(request, "sffrg/home.html", context)


def election_view(request):
    # Return the last five published questions.
    elections = Election.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    context = {
        'elections': elections
    }

    return render(request, "sffrg/index.html", context)


def candidate_view(request, election_id):
    # Return the last five published questions.
    candidates = Candidate.objects.all()
    context = {
        'candidates': candidates
    }

    return render(request, "sffrg/index2.html", context, election_id)


# class IndexView(generic.ListView):
#     template_name = 'sffrg/index.html'
#     context_object_name = 'latest_question_list'
#
#     def get_queryset(self):
#         # Return the last five published questions.
#         return Question.objects.filter(
#             pub_date__lte=timezone.now()
#         ).order_by('-pub_date')[:5]


# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'sffrg/detail.html'
#
#     def get_queryset(self):
#
#         # Excludes any questions that aren't published yet.
#
#         return Question.objects.filter(pub_date__lte=timezone.now())


# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'sffrg/results.html'
#
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         # request.POST accesses submitted data by key name, returns string
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'sffrg/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         # Redirects to another page and returns
#         return HttpResponseRedirect(reverse('sffrg:results', args=(question.id,)))
