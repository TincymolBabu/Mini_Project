from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('logdoc/', views.LoginDoc, name='logdoc'),
    path('signup/admin_dashboard',views.admin_dashboard, name='admin_dashboard'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('addsal/', views.addsal, name='addsal'),
    path('opt/', views.opt, name='opt'),
    path('register/opt/', views.opt, name='opt'),
    path('unapproved_employees/',views.unapproved_employees, name='unapproved_employees'),
    path('approve_employee/<int:employee_id>/',views.approve_employee, name='approve_employee'),
    path('emplog/', views.emplog, name='emplog'),
    path('employee_login/',views.employee_login, name='emplog'),
    path('emp_dashboard/', views.emp_dashboard, name='emp_dashboard'),
    path('atten/',views.atten,name='atten'),
    path('leave/',views.leave,name='leave'),
    path('emplogout/', views.logout, name='emplogout'),
    path('leave_request/', views.leave_request, name='leave_request'),
    path('leave1/', views.leave_request_list, name='leave_request_list'),
    #path('approve_leave/',views.approve_leave,name="approve_leave")


    path('unapproved_emplist/',views.unapproved_emplist, name='unapproved_emplist'),
    path('approve_emplist/<int:employee_id>/',views.approve_emplist, name='approve_emplist'),





]

