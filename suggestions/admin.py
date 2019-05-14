from django.contrib import admin

# Register your models here.
from suggestions.models import Suggestion

class SuggestionAdmin(admin.ModelAdmin):

    list_display = ['__str__', 'user']

    class Meta:
        model = Suggestion

admin.site.register(Suggestion, SuggestionAdmin)