from django.db.models import Sum
from django.shortcuts import get_object_or_404, render
from .models import Election, Candidate, Position, VotedUsers
from accounts.models import Account
from django.core.signing import Signer
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import serialization, hashes
# from cryptography.hazmat.primitives.asymmetric import padding
# from cryptography.hazmat.primitives.asymmetric import rsa
# from django.utils import crypto
# from django.http import Http404, HttpResponse, HttpResponseRedirect
# from django.urls import reverse


# def gen_key():
#     private_key = rsa.generate_private_key(
#         public_exponent=65537,
#         key_size=2048,
#         backend=default_backend()
#     )
#     return private_key
#
#
# def store_key():
#     with open("E:\Grad Project\suffrage\sffrg\key.pem", "wb") as key_file:
#         key_file.write(private_key.private_bytes(
#             encoding=serialization.Encoding.PEM,
#             format=serialization.PrivateFormat.TraditionalOpenSSL,
#             encryption_algorithm=serialization.NoEncryption()
#         ))

# priv = private_key.private_bytes(
#     encoding=serialization.Encoding.PEM,
#     format=serialization.PrivateFormat.TraditionalOpenSSL,
#     encryption_algorithm=serialization.NoEncryption()
# )
# Reads and designates private key from file
# with open("E:\Grad Project\suffrage\sffrg\key.pem", "rb") as key_file:
#     private_key = serialization.load_pem_private_key(
#         key_file.read(),
#         password=None,
#         backend=default_backend()
#     )
#
# # Derives private key from public key
# public_key = private_key.public_key()
#
# pub = private_key.public_key().public_bytes(
#     encoding=serialization.Encoding.PEM,
#     format=serialization.PublicFormat.SubjectPublicKeyInfo
# )


# Defines how the profile screen is presented to the user
def profile_view(request):
    users = Account.objects.all()

    # Passes off these values for use in the html file
    context = {
        'users': users
    }

    return render(request, "sffrg/profile.html", context)


def home_screen_view(request):
    # array, string or variable that can get referenced by html file

    user = request.user.id
    # if request.user.is_authenticated:
    #     fname = private_key.decrypt(
    #         request.user.first_name,
    #         padding.OAEP(
    #             mgf=padding.MGF1(algorithm=hashes.SHA256()),
    #             algorithm=hashes.SHA256(),
    #             label=None
    #         )
    #     )
    #     context = {
    #         'test_string': "Working as intended! This is the home screen.",
    #         'name': fname,
    #     }
    # else:
    context = {
        'test_string': "Working as intended! This is the home screen.",
    }
    return render(request, "sffrg/home.html", context)


def election_view(request):
    # Return the last five published questions.
    # elections = Election.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    elections = Election.objects.order_by('title')[:5]
    # election_votes = Election.objects.get(pk=election_id)

    context = {
        'elections': elections,
    }

    return render(request, "sffrg/elections.html", context)


def position_view(request, election_id):
    election_id = election_id

    positions = Election.objects.get(pk=election_id).position_set.all()

    context = {
        'positions': positions
    }

    return render(request, "sffrg/positions.html", context, election_id)


def candidate_view(request, election_id, position_id):
    election_id = election_id
    position_id = position_id
    # candidates = Candidate.objects.all()
    # candidates = Election.objects.get(pk=election_id).position.objects.get(pk=position_id).candidate_set.all()

    candidates = Position.objects.get(pk=position_id).candidate_set.all()

    vote_sum = candidates.aggregate(Sum('votes')).get('votes__sum', 0.00)
    # Pushes the total amount of votes back to database
    election_votes = Election.objects.get(pk=election_id)
    election_votes = Election.objects.get(pk=election_id)
    election_votes.total_votes = vote_sum
    election_votes.save()

    context = {
        'candidates': candidates,
    }

    return render(request, "sffrg/candidates.html", context, position_id)


def vote(request, election_id, position_id, candidate_id):
    selected_candidate = Candidate.objects.get(pk=candidate_id)
    # selected_candidate = selected_candidate.full_name

    # Base64 encoded SHA-1 hash
    signer = Signer()
    # Regular input
    # user = request.user.id
    # Hashes input
    user = signer.sign(request.user.id)
    temp = user.encode('UTF-8')

    # Encrypts input using RSA & Hashes suing SHA256
    # user_encrypted = public_key.encrypt(
    #     temp,
    #     padding.OAEP(
    #         mgf=padding.MGF1(algorithm=hashes.SHA256()),
    #         algorithm=hashes.SHA256(),
    #         label=None
    #         )
    # )
    # # Decrypts
    # original = private_key.decrypt(
    #     user_encrypted,
    #     padding.OAEP(
    #         mgf=padding.MGF1(algorithm=hashes.SHA256()),
    #         algorithm=hashes.SHA256(),
    #         label=None
    #     )
    # )
    #
    if VotedUsers.objects.filter(id=user, position=position_id).exists():
        voted = 1
        # selected_candidate.votes -= 1
        # selected_candidate.save()
    else:
        voted = 0
        selected_candidate.votes += 1
        selected_candidate.save()

        vu = VotedUsers(id=user, position=position_id)
        vu.save()

    context = {
        'selected_candidate': selected_candidate,
        'user': user,
        'pos': position_id,
        'voted': voted,
        # 'user_encrypted': user_encrypted,
        # 'original': original,
    }
    return render(request, "sffrg/vote.html", context, candidate_id)


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
