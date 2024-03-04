# from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import HRInfo
from .forms import JobDetailsForm
from django.core.exceptions import ObjectDoesNotExist


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

def recruitment(request):
    error_message = None
    if request.method == 'POST':
        form = JobDetailsForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                jobdetails = form.save(commit=False)
                try:
                    jobdetails.id = HRInfo.objects.get(username=request.POST['username'])
                    jobdetails.save()
                    print('Values saved to database:', jobdetails.jobtitle, jobdetails.jobfile, jobdetails.hr_info.username)
                    return redirect('jobcard.html')  # Redirect to the jobcard page after saving
                except ObjectDoesNotExist:
                    form.add_error('username', 'Username does not exist.')
                    error_message = 'Username does not exist.'
        except Exception as e:
            form.add_error(None, f"An error occurred: {e}")
            error_message = f"An error occurred: {e}"
    else:
        form = JobDetailsForm()
    return render(request, 'recruitment.html', {'form': form, 'error_message': error_message})


# def signup(request):
#     if request.method == 'POST':
#         try:
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             hr_info = HRInfo(username=username, password=password)
#             hr_info.save()
#             print('valuesssssssss::::::::::::',username,password)
#             return redirect('home.html')  # Redirect to the recruitment page after signup
#         # return HttpResponseRedirect('/home.html')  # Redirect to a success page
#         except Exception as e:
#                 # Handle the exception, e.g., log it or display an error message
#                 print(f"Error saving data to database: {e}")
#                 return HttpResponseRedirect('/error/')
#     else:
#         return render(request, 'signup.html')

# def signup(request):
#     if request.method == 'POST':
#         try:
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             print('Values received from form: username={}, password={}'.format(username, password))  # Print the received values
#             hr_info = HRInfo(username=username, password=password)
#             hr_info.save()
#             print('Values saved to database: username={}, password={}'.format(hr_info.username, hr_info.password))  # Print the saved values
#             return redirect('home.html')  # Redirect to the home page after signup
#         except Exception as e:
#             # Handle the exception, e.g., log it or display an error message
#             print(f"Error saving data to database: {e}")
#             return redirect('home')  # Redirect to the home page if an error occurs
#     else:
#         return render(request, 'signup.html')

# def signup(request):
#     if request.method == 'POST':
#         try:
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             # Check if the username already exists in the database
#             if HRInfo.objects.filter(username=username).exists():
#                 error_message = 'Username already exists. Please choose a different username.'
#                 return render(request, 'signup.html', {'error_message': error_message, 'username': username})
#             # Save the new user if the username is unique
#             hr_info = HRInfo(username=username, password=password)
#             hr_info.save()
#             print('Values saved to database: username={}, password={}'.format(hr_info.username, hr_info.password))
#             return redirect('home.html')  # Redirect to the home page after signup
#         except Exception as e:
#             # Handle the exception, e.g., log it or display an error message
#             print(f"Error saving data to database: {e}")
#             return redirect('signup.html')  # Redirect to the signup page if an error occurs
#     else:
#         return render(request, 'signup.html')

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
