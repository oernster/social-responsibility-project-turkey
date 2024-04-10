from django.contrib import admin
from django.urls import path
from questions.views import question_list, thank_you_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', question_list, name='question_list'),
    path('thank-you/', thank_you_view, name='thank_you'),
]
