from django.contrib import admin

from .models import Feedback, Support, Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'created_date', 'author', 'status', 'supporter')
    search_fields = ('text',)
    list_filter = ('created_date',)
    empty_value_display = '-пусто-'


class SupportAdmin(admin.ModelAdmin):
    list_display = ('supporter',)
    empty_value_display = '-пусто-'


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('message', 'sender', 'departure_date')
    empty_value_display = '-пусто-'


admin.site.register(Support, SupportAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Feedback, FeedbackAdmin)
