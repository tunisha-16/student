from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [

    path('', views.index, name='index'),
    path('login.html/', views.login, name='login'),
    path('submission.html/', views.submission, name='submission'),
    path('grade.html/', views.grade, name='grade'),
    path('forgotpassword.html/', views.forgotpassword, name='forgotpassword'),
    path('students.html', views.students, name='students'),
    path('faculty.html', views.faculty, name='faculty'),
    path('about.html', views.about, name='about'),
    path('viewcourses.html', views.courses, name='courses'),
    path('addcourse.html', views.add_course, name='add_course'),
    path('insertcourse/', views.insert_course, name='insertcourse'),
    path('adminhome.html', views.admin_home, name='admin_home'),
    path('students.html/', views.students, name='students'),
    path('contact.html/', views.contact, name='contact'),
]