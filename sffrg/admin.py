from django.contrib import admin
from sffrg.models import Election, Candidate

# admin.site.register(Election)


class CandidateAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ('election', 'full_name', 'state', 'party',),
                }
         ),
    ]


class CandidateInline(admin.TabularInline):
    model = Candidate
    extra = 3
    fieldsets = [
        (None, {
            'fields': ('election', 'full_name', 'state', 'party',),
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
    inlines = [CandidateInline]
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title']


admin.site.register(Election, ElectionAdmin)
admin.site.register(Candidate, CandidateAdmin)


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

