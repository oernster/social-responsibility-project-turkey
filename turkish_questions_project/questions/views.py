from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Question, UserResponse

@login_required
def question_list(request):
    if request.method == 'POST':
        # Process form submission
        for key, value in request.POST.items():
            if key.startswith('question_'):
                question_id = int(key.split('_')[1])
                response = value
                # Get or create UserResponse object
                user_response, created = UserResponse.objects.get_or_create(user=request.user, question_id=question_id)
                user_response.response = response
                user_response.save()

        # Redirect to thank you page to avoid form resubmission on page refresh
        return redirect('thank_you')

    else:
        # Render the template with initial or updated data
        questions = Question.objects.all()  
        user_responses = {response.question_id: response.response for response in UserResponse.objects.filter(user=request.user)}
        missed_questions = [question.id for question in questions if question.id not in user_responses]
        
        return render(request, 'question_list.html', {'questions': questions, 'user_responses': user_responses, 'missed_questions': missed_questions})

def thank_you_view(request):
    return render(request, 'thank_you.html')
