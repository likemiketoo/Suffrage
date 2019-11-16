from django.forms import TextInput, Textarea
from django.db import models
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from accounts.forms import AccountCreationForm
from accounts.models import Account
from sffrg.models import Election, Candidate, Position
from tinymce.widgets import TinyMCE

# admin.site.register(Election)


# Defines what user attributes are displayed and editable on the admin page
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


class CandidateAdmin(admin.ModelAdmin):

    list_display = ('full_name', 'position', 'state', 'party', 'election', 'position', 'votes')
    # Non-editable fields
    readonly_fields = ('votes',)

    fieldsets = [
        ('CANDIDATE INFO', {
            'fields': ('election', 'position', 'full_name', 'state', 'party', 'description', 'website', 'avatar',),
        }
        ),
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        # forms.ChoiceField: {'choices': ('President', 'Vice President', 'Secretary', 'Treasurer')},
    }


class CandidateInline(admin.TabularInline):
    model = Candidate
    extra = 3

    # fieldsets = [
    #     (None, {
    #         'fields': ('election', 'position', 'full_name', 'state', 'party', 'votes'),
    #     }
    #      ),
    # ]
    fieldsets = [
        (None, {
            'fields': ('election', 'full_name', 'state', 'party'),
        }
        ),
    ]

    def save_model(self, request, obj, form, change):
        obj.position = Position.objects.first()
        super(CandidateInline, self).save(request, obj, form, change)

    # Makes text box entry fields smaller
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '15'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
        # forms.ChoiceField: {'choices': ('President', 'Vice President', 'Secretary', 'Treasurer')},
    }
    readonly_fields = ('votes',)


class PositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'election')

    fieldsets = [
        ('Positions',
            {
                'fields': ['title']
            }
         ),
    ]

    inlines = [CandidateInline]


class PositionInline(admin.TabularInline):

    model = Position
    extra = 2

    fieldsets = [
        (None, {
            'fields': ('election', 'title'),
        }
         ),
    ]


class ElectionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
            {
                'fields': ['title', 'description']
            }
         ),
    ]
    inlines = [PositionInline]
    list_display = ('title', 'pub_date', 'total_votes')
    list_filter = ['pub_date']
    search_fields = ['title']


admin.site.register(Election, ElectionAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Position, PositionAdmin)

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

