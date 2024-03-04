# from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import HRInfo
from .forms import JobDetailsForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages



def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            hr_info = HRInfo.objects.get(username=username, password=password)
            return redirect('recruitment.html')  # Redirect to the recruitment page if credentials match
        except HRInfo.DoesNotExist:
            error_message = 'Username or password is incorrect. Please try again.'
            return render(request, 'home.html', {'error_message': error_message, 'username': username})
    else:
        return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def results(request):
    return results(request, 'results.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def jobcard(request):
    return render(request, 'jobcard.html')

def findee(request):
    return render(request, 'findee.html')

# def recruitment(request):
#     if request.method == 'POST':
#         form = JobDetailsForm(request.POST, request.FILES)
#         if form.is_valid():
#             jobdetails = form.save(commit=False)
#             jobdetails.id = HRInfo.objects.get(username=request.POST['username'])
#             jobdetails.save()
#             return redirect('home.html')  # Redirect to the home page after saving
#     else:
#         form = JobDetailsForm()
#     return render(request, 'recruitment.html', {'form': form})

# def results(request):
#     return render(request, 'results.html')

# def recruitment(request):
#     if request.method == 'POST':
#         form = JobDetailsForm(request.POST, request.FILES)
#         try:
#             if form.is_valid():
#                 jobdetails = form.save(commit=False)
#                 try:
#                     jobdetails.id = HRInfo.objects.get(username=request.POST['username'])
#                     jobdetails.save()
#                     print('Values saved to database:', jobdetails.jobtitle, jobdetails.jobdesc, jobdetails.hr_info.username)
#                     return redirect('jobcard.html')  # Redirect to the home page after saving
#                 except ObjectDoesNotExist:
#                     form.add_error('username', 'Username does not exist.')
#                     print('Error: Username does not exist.')
#         except Exception as e:
#             form.add_error(None, f"An error occurred: {e}")
#             print('Error saving values to database:', e)
#     else:
#         form = JobDetailsForm()
#     return render(request, 'recruitment.html', {'form': form})

# def recruitment(request):
#     error_message = None
#     if request.method == 'POST':
#         form = JobDetailsForm(request.POST, request.FILES)
#         try:
#             if form.is_valid():
#                 jobdetails = form.save(commit=False)
#                 try:
#                     jobdetails.id = HRInfo.objects.get(username=request.POST['username'])
#                     jobdetails.save()
#                     print('Values saved to database:', jobdetails.jobtitle, jobdetails.jobfile, jobdetails.hr_info.username)
#                     return redirect('jobcard.html')  # Redirect to the jobcard page after saving
#                 except ObjectDoesNotExist:
#                     form.add_error('username', 'Username does not exist.')
#                     error_message = 'Username does not exist.'
#         except Exception as e:
#             form.add_error(None, f"An error occurred: {e}")
#             error_message = f"An error occurred: {e}"
#     else:
#         form = JobDetailsForm()
#     return render(request, 'recruitment.html', {'form': form, 'error_message': error_message})

# def recruitment(request):
#     error_message = None
#     if request.method == 'POST':
#         form = JobDetailsForm(request.POST, request.FILES)
#         if form.is_valid():
#             try:
#                 jobdetails = form.save()
#                 print('Values saved to database:', jobdetails.jobtitle, jobdetails.jobfile, jobdetails.hr_info.username)
#                 messages.success(request, 'Job posted successfully!')
#                 return redirect('jobcard.html')  # Redirect to the jobcard page after saving
#             except Exception as e:
#                 form.add_error(None, f"An error occurred: {e}")
#                 error_message = f"An error occurred: {e}"
#                 messages.error(request, 'Failed to post job.')

#     else:
#         form = JobDetailsForm()
#     return render(request, 'recruitment.html', {'form': form, 'error_message': error_message})

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import JobDetailsForm

# def recruitment(request):
#     print("hiiiiiiiii;;;;;;;;;;;;;")
#     error_message = None
#     print("hiiiiiiiii2222222222222")

#     if request.method == 'POST':
#         print("hi;333333333;;;;;;;")
#         form = JobDetailsForm(request.POST, request.FILES)
#         print("hi;444444444;;;;;;;")

#         if form.is_valid():
#             print("hi555555555;;;;;;;")
#             try:
#                 print("hi;;;;66666666666;;;;;")
#                 # jobdetails=JobDetailsForm(jobtitle=jobtitle,jobfile=jobfile)
#                 # jobdetails = form.save()
#                 jobdetails = form.save(commit=False)  # Don't save the form to database yet
#                  # Assuming `hr_info` is a ForeignKey field that should be set to the current user's HRInfo
#                 print("hi;;;;7777777777777;;;;;")
#                 hr_info_id = request.user.hrinfo.id
#                 print("hi;;;;77777777788888;;;;;")
#                 jobdetails.hr_info_id = hr_info_id
#                 print("ppppppppppppppp;;;")
#                 jobdetails.hr_info = request.user.hr_info  # PROBLEM::::Assuming `request.user.hr_info` is the HRInfo object for the current user
#                 print("hi;;;;888888888;;;;;")
#                 jobdetails.save()  # Save the JobDetails instance with the HRInfo set
#                 print('Values saved to database:', jobdetails.jobtitle, jobdetails.jobfile, jobdetails.hr_info.username)
#                 messages.success(request, 'Job posted successfully!')
#                 return redirect('jobcard.html')  # Redirect to the jobcard page after saving
#             except Exception as e:
#                 form.add_error(None, f"An error occurred: {e}")
#                 error_message = f"An error occurred: {e}"
#                 messages.error(request, 'Failed to post job.')
#     else:
#         form = JobDetailsForm()
#     return render(request, 'recruitment.html', {'form': form, 'error_message': error_message})

#nextttt one
def recruitment(request):
    # Initialize error message to None
    error_message = None

    # Print statement to indicate the start of the view function
    print("Start of recruitment view")

    if request.method == 'POST':
        # Print statement to indicate that a POST request is received
        print("POST request received")
        
        # Create a form instance with the POST data and files
        form = JobDetailsForm(request.POST, request.FILES)
        
        # Check if the form is valid
        if form.is_valid():
            # Print statement to indicate that the form is valid
            print("Form is valid")
            try:
                # Create an instance of JobDetails but don't save it to the database yet
                jobdetails = form.save(commit=False)
                print('1;;;;;;;;;;;;;222')
                # Get the id of the HRInfo object associated with the current user
                hr_info_id = request.user.hrinfo.id
                print('iii;;;;;;;;i')
                # Set the hr_info_id field of jobdetails
                jobdetails.hr_info_id = hr_info_id
                print("id;;;;;;;;;;;;;;;",hr_info_id)
                # Save the jobdetails instance to the database
                jobdetails.save()
                
                # Print values saved to the database
                print('Values saved to database:', jobdetails.jobtitle, jobdetails.jobfile, jobdetails.hr_info.username)
                
                # Add a success message
                messages.success(request, 'Job posted successfully!')
                
                # Redirect to the jobcard.html page
                return redirect('jobcard.html')
            except Exception as e:
                # If an exception occurs, add the error to the form
                form.add_error(None, f"An error occurred: {e}")
                # Set the error message
                error_message = f"An error occurred: {e}"
                # Add an error message
                messages.error(request, 'Failed to post job.')
    else:
        # If the request method is not POST, create an empty form
        form = JobDetailsForm()
    
    # Render the recruitment.html template with the form and error_message
    return render(request, 'recruitment.html', {'form': form, 'error_message': error_message})



def signup(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            # Check if the username already exists in the database
            if HRInfo.objects.filter(username=username).exists():
                error_message = 'Username already exists. Please choose a different username.'
                return render(request, 'signup.html', {'error_message': error_message, 'username': username})
            # Save the new user if the username is unique
            hr_info = HRInfo(username=username, password=password)
            hr_info.save()
            print('Values saved to database: username={}, password={}'.format(hr_info.username, hr_info.password))
            return redirect('home.html')  # Redirect to the home page after signup
        except Exception as e:
            # Handle the exception, e.g., log it or display an error message
            print(f"Error saving data to database: {e}")
            return redirect('signup.html')  # Redirect to the signup page if an error occurs
    else:
        error_message = 'Please enter a username and password.'
        return render(request, 'signup.html', {'error_message': error_message})
