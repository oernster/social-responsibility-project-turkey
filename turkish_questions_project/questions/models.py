from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    text = models.TextField(verbose_name='Soru')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Soru'
        verbose_name_plural = 'Sorular'

class UserResponse(models.Model):
    RESPONSE_CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No'),
        ('dont_know', "I don't know"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Kullanıcı')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Soru')
    response = models.CharField(max_length=20, choices=RESPONSE_CHOICES, verbose_name='Cevap')

    def __str__(self):
        return f'{self.question}: {self.get_response_display()}'

    class Meta:
        verbose_name = 'Kullanıcı Cevabı'
        verbose_name_plural = 'Kullanıcı Cevapları'

