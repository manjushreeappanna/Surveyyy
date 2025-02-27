# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.core.mail import send_mail
# from .models import Survey
# from .forms import SurveyForm, UserRegistrationForm
# from django.contrib.auth.decorators import login_required
# import random
# import string

# from django.core.mail import send_mail
# from django.shortcuts import render, redirect
# from .forms import UserRegistrationForm
# import random
# import string

# def generate_temp_password():
#     return ''.join(random.choices(string.ascii_letters + string.digits, k=8)) 

# def send_survey_link(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             temp_password = generate_temp_password()
#             user.set_password(temp_password)  # Use a random temporary password
#             user.save()

#             # Generate the survey link
#             link = f"http://127.0.0.1:8000/survey_app/{user.id}/"

#             # Send the email
#             send_mail(
#                 'Survey Link',
#                 f'Click this link to fill out the survey: {link}\nYour temporary password: {temp_password}',
#                 'your_real_email@gmail.com',  # Must match EMAIL_HOST_USER in settings.py
#                 [user.email]
#             )
#             return redirect('survey_sent')
#     else:
#         form = UserRegistrationForm()

#     return render(request, 'survey_app/send_survey.html', {'form': form})



# # def send_survey_link(request):
# #     if request.method == 'POST':
# #         form = UserRegistrationForm(request.POST)
# #         if form.is_valid():
# #             user = form.save(commit=False)
# #             user.set_password('temp_password')  # Temporary password
# #             user.save()
# #             link = f"http://127.0.0.1:8000/survey_app/{user.id}/"
# #             send_mail(
# #                 'Survey Link',
# #                 f'Click this link to fill out the survey: {link}',
# #                 'prarthanauthappa713@gmail.com',
# #                 [user.email]
# #             )
# #             return redirect('survey_sent')
# #     else:
# #         form = UserRegistrationForm()
# #     return render(request, 'survey_app/send_survey.html', {'form': form})

# # def fill_survey(request, user_id):
# #     survey, created = Survey.objects.get_or_create(user_id=user_id)
# #     user = User.objects.get(id=user_id)
# #     if request.method == 'POST':
# #         form = SurveyForm(request.POST)
# #         if form.is_valid():
# #             survey = form.save(commit=False)
# #             survey.user = user
# #             survey.save()
# #             return redirect('survey_submitted')
        
# #     else:
# #         form = SurveyForm()
# #     return render(request, 'survey_app/fill_survey.html', {'form': form})




# def fill_survey(request, user_id):
#     survey, created = Survey.objects.get_or_create(user_id=user_id)  # Get existing survey or create a new one
#     if request.method == 'POST':
#         survey.tea = request.POST.get('tea', 0)
#         survey.coffee = request.POST.get('coffee', 0)
#         survey.biscuit = request.POST.get('biscuit', 0)
#         survey.smoking = request.POST.get('smoking', 0)
#         survey.save()  # Save the changes instead of creating a duplicate
        
#         return redirect('survey_submitted')  # Redirect after saving

#     return render(request, 'survey_app/fill_survey.html', {'survey': survey})




# def approve_survey(request, survey_id):
#     survey = Survey.objects.get(id=survey_id)
#     survey.is_approved = True
#     survey.save()
    
#     password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
#     user = survey.user
#     user.set_password(password)
#     user.save()
    
#     send_mail(
#         'Your Account Details',
#         f'Your password: {password}\nLogin here: http://127.0.0.1:8000/login/',
#         'your_email@example.com',
#         [user.email]
#     )
    
#     return redirect('survey_approved')



# @login_required
# def user_homepage(request):
#     survey = Survey.objects.get(user=request.user)
#     monthly_expenses = (survey.tea + survey.coffee +
#                        survey.biscuit + survey.smoking) * 30
#     weekly_expenses = monthly_expenses / 4
#     daily_expenses = monthly_expenses / 30

#     context = {
#         'survey': survey,
#         'daily_expenses': daily_expenses,
#         'weekly_expenses': weekly_expenses,
#         'monthly_expenses': monthly_expenses
#     }
#     return render(request, 'survey_app/user_home.html', context)


# from django.shortcuts import render, get_object_or_404
# from .models import Survey

# def user_homepage(request):
#     user = request.user  # Get the logged-in user
    
#     # Check if a survey exists for the user
#     survey = Survey.objects.filter(user=user).first()  # Use .first() to avoid DoesNotExist error

#     if not survey:
#         return render(request, "survey_app/user_home.html", {"message": "No survey data available."})
#     print(f"Survey Data: Tea={survey.tea}, Coffee={survey.coffee}, Biscuit={survey.biscuit}, Smoking={survey.smoking}")
    
#     context = {
#         "user": user,
#         "tea": survey.tea if survey.tea else 0,
#         "coffee": survey.coffee if survey.coffee else 0,
#         "biscuit": survey.biscuit if survey.biscuit else 0,
#         "smoking": survey.smoking if survey.smoking else 0,
#         "daily_expenses": survey.daily_expenses if survey.daily_expenses else 0,
#         "weekly_expenses": survey.weekly_expenses if survey.weekly_expenses else 0,
#         "monthly_expenses": survey.monthly_expenses if survey.monthly_expenses else 0,
#     }
#     return render(request, "survey_app/user_home.html", context)



# def survey_submitted(request):
#     return render(request, "survey_app/survey_submitted.html")



# import matplotlib.pyplot as plt
# import io
# import urllib
# import base64

# def expense_analytics(request):
#     # Fetch all user survey responses
#     responses = Survey.objects.all()

#     surveys = Survey.objects.all()
#     daily_expenses = [survey.tea + survey.coffee + survey.biscuit + survey.smoking for survey in surveys]

#     # Aggregate data
#     daily_expenses = sum([r.daily_expenses for r in responses])
#     weekly_expenses = daily_expenses * 7
#     monthly_expenses = daily_expenses * 30

#     # Data for visualization
#     labels = ["Daily", "Weekly", "Monthly"]
#     values = [daily_expenses, weekly_expenses, monthly_expenses]

#     # Generate graph
#     plt.figure(figsize=(6, 4))
#     plt.bar(labels, values, color=['blue', 'orange', 'green'])
#     plt.xlabel("Expense Period")
#     plt.ylabel("Amount Spent")
#     plt.title("User Expense Analytics")

#     # Convert plot to image
#     buf = io.BytesIO()
#     plt.savefig(buf, format='png')
#     buf.seek(0)
#     string = base64.b64encode(buf.getvalue()).decode('utf-8')
#     uri = 'data:image/png;base64,' + string
#     plt.close()

#     return render(request, "survey_app/analytics.html", {"graph": uri})




# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.models import User
# from django.core.mail import send_mail
# from django.contrib.auth.decorators import login_required
# from .models import Survey
# from .forms import SurveyForm, UserRegistrationForm
# import random
# import string
# import matplotlib.pyplot as plt
# import io
# import urllib
# import base64


# def generate_temp_password():
#     return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

# def send_survey_link(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             temp_password = generate_temp_password()
#             user.set_password(temp_password)
#             user.save()

#             survey_link = f"http://127.0.0.1:8000/survey_app/{user.id}/"
#             send_mail(
#                 'Survey Link',
#                 f'Click this link to fill out the survey: {survey_link}\nYour temporary password: {temp_password}',
#                 'prarthanauthappa713@gmail.com',  # Ensure this matches EMAIL_HOST_USER in settings.py
#                 [user.email]
#             )
#             return redirect('survey_sent')

#     else:
#         form = UserRegistrationForm()

#     return render(request, 'survey_app/send_survey.html', {'form': form})

# # Fill Survey
# def fill_survey(request, user_id):
#     survey = Survey.objects.filter(user_id=user_id).first()  # Avoid unnecessary object creation
#     if not survey:
#         survey = Survey(user_id=user_id)

#     if request.method == 'POST':
#         survey.tea = int(request.POST.get('tea', 0))
#         survey.coffee = int(request.POST.get('coffee', 0))
#         survey.biscuit = int(request.POST.get('biscuit', 0))
#         survey.smoking = int(request.POST.get('smoking', 0))
#         survey.save()  
        
#         return redirect('survey_submitted')

#     return render(request, 'survey_app/fill_survey.html', {'survey': survey})

# # Approve Survey
# def approve_survey(request, survey_id):
#     survey = get_object_or_404(Survey, id=survey_id)
#     survey.is_approved = True
#     survey.save()
    
#     user = get_object_or_404(User, id=survey.user.id)
#     password = generate_temp_password()
#     user.set_password(password)
#     user.save()
    
#     send_mail(
#         'Your Account Details',
#         f'Your password: {password}\nLogin here: http://127.0.0.1:8000/login/',
#         'your_email@example.com',
#         [user.email]
#     )
    
#     return redirect('survey_approved')

# # User Homepage with Expense Summary
# @login_required
# def user_homepage(request):
#     survey = Survey.objects.filter(user=request.user).first()

#     if not survey:
#         return render(request, "survey_app/user_home.html", {"message": "No survey data available."})
    
#     daily_expenses = (survey.tea + survey.coffee + survey.biscuit + survey.smoking)
#     weekly_expenses = daily_expenses * 7
#     monthly_expenses = daily_expenses * 30

#     context = {
#         "user": request.user,
#         "survey": survey,
#         "daily_expenses": daily_expenses,
#         "weekly_expenses": weekly_expenses,
#         "monthly_expenses": monthly_expenses
#     }
#     return render(request, "survey_app/user_home.html", context)

# # Survey Submitted Page
# def survey_submitted(request):
#     return render(request, "survey_app/survey_submitted.html")

# # Expense Analytics (Visualization)
# def expense_analytics(request):
#     surveys = Survey.objects.all()

#     # Calculate expenses
#     daily_expenses = sum(survey.tea + survey.coffee + survey.biscuit + survey.smoking for survey in surveys)
#     weekly_expenses = daily_expenses * 7
#     monthly_expenses = daily_expenses * 30

#     # Bar Chart
#     labels = ["Daily", "Weekly", "Monthly"]
#     values = [daily_expenses, weekly_expenses, monthly_expenses]

#     plt.figure(figsize=(6, 4))
#     plt.bar(labels, values, color=['blue', 'orange', 'green'])
#     plt.xlabel("Expense Period")
    # plt.ylabel("Amount Spent")
    # plt.title("User Expense Analytics")

    # # Convert plot to image
    # buf = io.BytesIO()
    # plt.savefig(buf, format='png')
    # buf.seek(0)
    # string = base64.b64encode(buf.getvalue()).decode('utf-8')
    # uri = 'data:image/png;base64,' + string
    # plt.close()

    # return render(request, "survey_app/analytics.html", {"graph": uri})




from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Survey
from .forms import SurveyForm, UserRegistrationForm
import random
import string
import matplotlib.pyplot as plt
import io
import urllib
import base64

# Function to generate a random temporary password
def generate_temp_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8)) 

# Send Survey Link to Users via Email
def send_survey_link(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            temp_password = generate_temp_password()
            user.set_password(temp_password)  # Set a temporary password
            user.save()

            # Generate the survey link
            link = f"http://127.0.0.1:8000/survey_app/{user.id}/"

            # Send email with survey link
            send_mail(
                'Survey Invitation',
                f'Click the link to fill out the survey: {link}\nYour temporary password: {temp_password}',
                settings.EMAIL_HOST_USER,  # Ensure EMAIL_HOST_USER is set in settings.py
                [user.email],
                fail_silently=False,
            )
            return redirect('survey_sent')  # Redirect after sending email
    else:
        form = UserRegistrationForm()

    return render(request, 'survey_app/send_survey.html', {'form': form})

# Function to allow users to fill out their survey
def fill_survey(request, user_id):
    survey, created = Survey.objects.get_or_create(user_id=user_id)  # Get existing survey or create a new one
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            survey.tea = request.POST.get('tea', 0)
            survey.coffee = request.POST.get('coffee', 0)
            survey.biscuit = request.POST.get('biscuit', 0)
            survey.smoking = request.POST.get('smoking', 0)
            survey.save()  # Save the survey data

    return render(request, 'survey_app/fill_survey.html', {'survey': survey})
def survey_sent(request):
    return render(request, "survey_app/survey_sent.html")

def approve_survey(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)
    survey.is_approved = True
    survey.save()

    password = generate_temp_password()
    user = survey.user
    user.set_password(password)
    user.save()
    
    
    send_mail(
        'Your Account Details',
        f'Your password: {password}\nLogin here: http://127.0.0.1:8000/login/',
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False
    )
    
    return redirect('survey_approved')


# User dashboard displaying survey results and expense calculations
@login_required
def user_homepage(request):
    user = request.user
    survey = Survey.objects.filter(user=user).first()

    if not survey:
        return render(request, "survey_app/user_home.html", {"message": "No survey data available."})

    monthly_expenses = (survey.tea + survey.coffee + survey.biscuit + survey.smoking) * 30
    weekly_expenses = monthly_expenses / 4
    daily_expenses = monthly_expenses / 30

    context = {
        "user": user,
        "survey": survey,
        "daily_expenses": daily_expenses,
        "weekly_expenses": weekly_expenses,
        "monthly_expenses": monthly_expenses,
    }
    return render(request, "survey_app/user_home.html", context)

# View to render the survey submitted confirmation page
def survey_submitted(request):
    return render(request, "survey_app/survey_submitted.html")

# Expense analytics visualization using Matplotlib
def expense_analytics(request):
    surveys = Survey.objects.all()
    
    if not surveys:
        return render(request, "survey_app/analytics.html", {"message": "No data available."})

    # Calculate total daily, weekly, and monthly expenses
    total_daily_expenses = sum([s.tea + s.coffee + s.biscuit + s.smoking for s in surveys])
    total_weekly_expenses = total_daily_expenses * 7
    total_monthly_expenses = total_daily_expenses * 30

    # Data for bar chart
    labels = ["Daily", "Weekly", "Monthly"]
    values = [total_daily_expenses, total_weekly_expenses, total_monthly_expenses]

    # Generate bar chart
    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color=['blue', 'orange', 'green'])
    plt.xlabel("Expense Period")
    plt.ylabel("Amount Spent")
    plt.title("User Expense Analytics")

    # Convert plot to image
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.getvalue()).decode('utf-8')
    uri = 'data:image/png;base64,' + string
    plt.close()

    return render(request, "survey_app/analytics.html", {"graph": uri})
