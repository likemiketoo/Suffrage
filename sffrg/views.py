from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from .models import Election, Candidate
from accounts.models import Account


# Defines how the profile screen is presented to the user
def profile_view(request):
    users = Account.objects.all()

    # Passes off these values for use in the html file
    context = {
        'users': users
    }

    return render(request, "sffrg/profile.html", context)


# Defines how the main splash is presented to the user
def home_screen_view(request):
    # array, string or variable that can get referenced by html file
    # tot = Candidate.objects.aggregate(Sum('votes')).get('votes__sum', 0.00)

    # Passes off these values for use in the html file
    context = {
        'test_string': "Working as intended! This is the home screen.",
    }
    return render(request, "sffrg/home.html", context)


# Defines how the election screen is presented to the user
def election_view(request):
    # Return the last five published questions.
    # elections = Election.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    elections = Election.objects.order_by('title')[:5]

    # Passes off these values for use in the html file
    context = {
        'elections': elections
    }

    return render(request, "sffrg/elections.html", context)


# Defines how the candidate screen is presented to the user
def candidate_view(request, election_id):
    # Return the last five published questions.
    election_id = election_id
    # candidates = Candidate.objects.all()
    candidates = Election.objects.get(pk=election_id).candidate_set.all()
    # Adds up candidate votes of this election, and returns the number
    vote_sum = candidates.aggregate(Sum('votes')).get('votes__sum', 0.00)
    # Pushes the total amount of votes back to database
    election_votes = Election.objects.get(pk=election_id)
    election_votes.total_votes = vote_sum
    election_votes.save()

    # Passes off these values for use in the html file
    context = {
        'candidates': candidates,
    }

    return render(request, "sffrg/candidates.html", context, election_id)


# class IndexView(generic.ListView):
#     template_name = 'sffrg/elections.html'
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
