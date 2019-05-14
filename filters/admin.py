from django.contrib import admin

# Register your models here.
from filters.models import Filter, NegativeFilter

admin.site.register(Filter)
admin.site.register(NegativeFilter)