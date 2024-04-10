from django.contrib import admin
from .models import Question, UserResponse

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text',)
    search_fields = ('text',)

admin.site.register(Question, QuestionAdmin)

class UserResponseAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'response')
    list_filter = ('response',)
    search_fields = ('user__username', 'question__text',)
    raw_id_fields = ('user', 'question',)

admin.site.register(UserResponse, UserResponseAdmin)
