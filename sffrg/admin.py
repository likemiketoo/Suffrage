from django.forms import TextInput, Textarea
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from sffrg.models import Election, Candidate
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from accounts.forms import AccountCreationForm
from accounts.models import Account


class AccountAdmin(UserAdmin):
    add_form = AccountCreationForm
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin',)
    search_fields = ('email', 'username',)

    # Only allows certain fields to be editable on creation
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['dob']
        else:
            return []

    readonly_fields = ('date_joined', 'last_login', 'dob',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = [
        ('USER INFO', {
            'fields': ('email', 'first_name', 'last_name', 'username', 'zip_code', 'dob',),
                }
         ),
    ]

    add_fieldsets = [
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'username', 'zip_code', 'dob')}
         ),
    ]


# Dictates what candidate fields are viewable/editable from the admin console
class CandidateAdmin(admin.ModelAdmin):
    # What's displayed on the summary screen
    list_display = ('full_name', 'state', 'party', 'votes', 'election')
    # Non-editable fields
    readonly_fields = ('votes', )

    fieldsets = [
        ('CANDIDATE INFO', {
            'fields': ('election', 'full_name', 'state', 'party',),
                }
         ),
    ]


# Candidate options within elections
class CandidateInline(admin.TabularInline):
    model = Candidate
    extra = 0
    fieldsets = [
        (None, {
            'fields': ('election', 'full_name', 'state', 'party', 'votes'),
        }
         ),
    ]
    # Makes text box entry fields smaller
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '15'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }
    readonly_fields = ('votes',)


# Dictates what election fields are viewable/editable from the admin console
class ElectionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('ELECTION INFO',
            {
                'fields': ['title', 'description']
            }
         ),
    ]

    # Candidate.objects.aggregate(Sum('votes')).get('votes__sum', 0.00)

    inlines = [CandidateInline]
    list_display = ('title', 'pub_date', 'total_votes')
    list_filter = ['pub_date']
    search_fields = ['title']


admin.site.register(Election, ElectionAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Account, AccountAdmin)


# from .models import Choice, Question
#
#
# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3
#
#
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]
#     list_display = ('question_text', 'pub_date', 'was_published_recently')
#     list_filter = ['pub_date']
#     search_fields = ['question_text']
#
#
# admin.site.register(Question, QuestionAdmin)

