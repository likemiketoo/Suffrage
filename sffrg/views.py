from django.db.models import Sum, F
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Election, Candidate, Position, VotedUsers
from accounts.models import Account
from django.core import signing
from django.core.signing import Signer


# Defines how the profile screen is presented to the user
def profile_view(request):
    users = Account.objects.all()

    # Passes off these values for use in the html file
    context = {
        'users': users
    }

    return render(request, "sffrg/profile.html", context)


def home_screen_view(request):
    # Declares fernet encryption method
    signer = Signer(request.user.id)
    # Gets user value for
    user = request.user
    vu = VotedUsers.objects.all()
    if user.is_authenticated:
    #
    #     # Checks to see if any inputs have been tampered and fail unsigning, and removes them
    #     for voters in vu:
    #         try:
    #             test = signer.unsign(voters.id)
    #         except signing.BadSignature:
    #             malicious_voter = VotedUsers.objects.get(id=voters.id)
    #             malicious_voter.delete()
    #
    #     # Checks to see if theres any values that passed signing, but aren't from registed users and removes them
    #     for voters in vu:
    #         original_id = signer.unsign(voters.id)
    #         if Account.objects.filter(id=original_id).exists():
    #             pass
    #         else:
    #             malicious_voter = VotedUsers.objects.get(id=voters.id)
    #             malicious_voter.delete()

        context = {
            'test_string': "Start Voting!",
        }

        return render(request, "sffrg/home.html", context)
    else:
        return render(request, "sffrg/home.html")


def election_view(request):
    # Return the last ten published questions.
    elections = Election.objects.order_by('title')[:5]
    elect = Election.objects.all()
    for elecs in elect:
        # candidates = Position.objects.get(election=elecs.id).candidate_set.all()
        candidates = Candidate.objects.all().filter(election=elecs.id).all()
        vote_sum = candidates.aggregate(Sum('votes')).get('votes__sum', 0.00)
        elecs.total_votes = vote_sum
        elecs.save()

    context = {
        'elections': elections,
        'candidates': candidates,
    }

    return render(request, "sffrg/elections.html", context)


def position_view(request, election_id):
    election_id = election_id

    signer = Signer(request.user.id)
    election_signed = signer.sign(election_id)
    # election_unsigned = signer.unsign(election_signed)

    positions = Election.objects.get(pk=election_id).position_set.all()
    for position in positions:
        position.id = signer.sign(position.id)

    context = {
        'positions': positions,
        'election_signed': election_signed,
    }

    return render(request, "sffrg/positions.html", context, election_signed)


def candidate_view(request, position_signed):
    # election_id = election_id
    # position_id = position_id
    signer = Signer(request.user.id)
    position_unsigned = signer.unsign(position_signed)
    user = signer.sign(request.user.id)

    if request.method == 'POST':
        context = {
            'test_string': "POST function is working correctly",
        }
        return render(request, "sffrg/home.html", context)

    if VotedUsers.objects.filter(id=user, position=position_unsigned).exists():
        voted = 1
        context = {
            'voted': voted,
        }
        return render(request, "sffrg/candidates.html", context, position_signed)

    else:
        voted = 0
        candidates = Position.objects.get(pk=position_unsigned).candidate_set.all()
        for candidate in candidates:
            candidate.id = signer.sign(candidate.id)

        # vote_sum = candidates.aggregate(Sum('votes')).get('votes__sum', 0.00)
        # # Pushes the total amount of votes back to database
        # election_votes = Election.objects.get(pk=election_id)
        # election_votes.total_votes = vote_sum
        # election_votes.save()
        context = {
            'candidates': candidates,
            'voted': voted,
        }

        return render(request, "sffrg/candidates.html", context, position_signed)


def vote(request, candidate_signed):
    signer = Signer(request.user.id)
    candidate_unsigned = signer.unsign(candidate_signed)

    selected_candidate = Candidate.objects.get(pk=candidate_unsigned)
    position_id = selected_candidate.position.id
    voted = None
    # selected_candidate = selected_candidate.full_name

    # Base64 encoded SHA-1 hash
    user = signer.sign(request.user.id)

    # If vote has voter before, block them from viewing or voting again.
    if VotedUsers.objects.filter(id=user, position=position_id).exists():
        voted = 1

    # After user presses submit button, execute post statement and lock user out from voting again
    else:
        voted = 0
        if request.method == "POST":
            voted = 1
            # selected_candidate.votes += 1
            selected_candidate.votes = F('votes') + 1
            selected_candidate.save()
            vu = VotedUsers(id=user, position=position_id)
            vu.save()

    # vu = VotedUsers.objects.all()
    # if user.is_authenticated:
    #     # Checks to see if any inputs have been tampered and fail unsigning, and removes them
    #     for voters in vu:
    #         try:
    #             test = signer.unsign(voters.id)
    #         except signing.BadSignature:
    #             malicious_voter = VotedUsers.objects.get(id=voters.id)
    #             malicious_voter.delete()
    #
    #     # Checks to see if theres any values that passed signing, but aren't from registed users and removes them
    #     for voters in vu:
    #         original_id = signer.unsign(voters.id)
    #         if Account.objects.filter(id=original_id).exists():
    #             pass
    #         else:
    #             malicious_voter = VotedUsers.objects.get(id=voters.id)
    #             malicious_voter.delete()
    #
    #     return render(request, "sffrg/home.html", context)
    # else:
    #     return render(request, "sffrg/home.html")
    #
    # context = {
    #     'selected_candidate': selected_candidate,
    #     'user': user,
    #     'pos': position_id,
    #     'voted': voted,
    # }
    return render(request, "sffrg/vote.html", context, candidate_signed)


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
