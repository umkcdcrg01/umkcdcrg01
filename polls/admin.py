from django.contrib import admin
from polls.models import Poll, Choice, Result

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	# make the display order for model fields
	# fields = ['pub_date', 'question']

	# fieldsets will put contents in seperate frame
	# fieldsets = [
	# 	(None, 				{'fields': ['question']}),
	# 	('Date information', {'fields': ['pub_date']}),
	# ]
	list_display = ('question', 'pub_date', 'was_published_recently')
	inlines = [ChoiceInline]
	list_filter = ['pub_date']
	search_field = ['question']

# class ChoiceAdmin(admin.ModelAdmin):
# 	#fields = ['poll', 'votes', 'choice_text']

# 	fieldsets = [
# 		('poll', 		{'fields': ['poll']}),
# 		('choice_text', {'fields': ['choice_text']}),
# 		('votes', 		{'fields': ['votes']}),
# 	]
# Register your models here.
admin.site.register(Poll, PollAdmin)
#admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Result)


# Or you can just use admin.site.register(Poll)