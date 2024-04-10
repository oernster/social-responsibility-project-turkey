from django.test import TestCase
from django.contrib.auth.models import User
from .models import Question, UserResponse

class QuestionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Question.objects.create(text='Test Question')

    def test_text_label(self):
        question = Question.objects.get(id=1)
        field_label = question._meta.get_field('text').verbose_name
        self.assertEqual(field_label, 'Soru')

    def test_text_max_length(self):
        question = Question.objects.get(id=1)
        max_length = question._meta.get_field('text').max_length
        self.assertEqual(max_length, 400)

class UserResponseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='testuser', password='password')
        question = Question.objects.create(text='Test Question')
        UserResponse.objects.create(user=user, question=question, response='yes')

    def test_user_label(self):
        user_response = UserResponse.objects.get(id=1)
        field_label = user_response._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'Kullanıcı')

    def test_response_label(self):
        user_response = UserResponse.objects.get(id=1)
        field_label = user_response._meta.get_field('response').verbose_name
        self.assertEqual(field_label, 'Cevap')

    def test_response_choices(self):
        user_response = UserResponse.objects.get(id=1)
        choices = dict(user_response.RESPONSE_CHOICES)
        self.assertEqual(choices['yes'], 'Yes')
        self.assertEqual(choices['no'], 'No')
        self.assertEqual(choices['dont_know'], "I don't know")
