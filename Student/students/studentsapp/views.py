from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    # Your index view logic here
    return render(request, 'index.html')

def login(request):
    # Your login view logic here
    return render(request, 'login.html')

def submission(request):
    # Your login view logic here
    return render(request, 'submission.html')

def grade(request):
    # Your logic to render the grade.html page goes here
    return render(request, 'grade.html')

def forgotpassword(request):
    # Your logic to render the grade.html page goes here
    return render(request, 'forgotpassword.html')

from django.shortcuts import render

def students(request):
    return render(request, 'students.html')

def view_students(request):
    # Your view logic goes here
    return render(request, 'students.html')


def faculty(request):
    return render(request, 'faculty.html')

def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'viewcourses.html')


def add_course(request):
    return render(request, 'addcourse.html')

def insert_course(request):
    # Handle inserting a new course logic here
    return HttpResponse("Course inserted successfully!")

def admin_home(request):
    # Add any necessary logic here
    return render(request, 'adminhome.html')

def default_redirect_view(request):
    return redirect('admin_home')

def contact(request):
    return render(request, 'contact.html')