from django.contrib import admin
from .models import StatisticsData

class StatisticsDataAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

admin.site.register(StatisticsData, StatisticsDataAdmin)
