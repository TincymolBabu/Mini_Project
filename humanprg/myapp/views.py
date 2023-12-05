
from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Employee,Employeelist
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm,LeaveRequestApprovalForm
from django.contrib import messages
from .models import LeaveApplication

from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    return render(request,'home.html')
def admin_dashboard(request):
    return render(request,'admin.html')

#login
def LoginDoc(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request,'login.html')

def register(request):
    return render(request,'registration.html')

#logout

def logout(request):
    return render(request,'home.html')

#add salary

def addsal(request):
    return render(request,'addsalary.html')

#employee signin signup

def opt(request):
    return render(request,'options.html')




def register(request):
    if request.method == 'POST':
        employeeid = request.POST['employeeid']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        dob = request.POST['dob']
        address = request.POST['address']
        mobile = request.POST['mobile']
        emailid = request.POST['emailid']
        department = request.POST['department']
        salary = request.POST['salary']
        username = request.POST['username']
        password = request.POST['password']

        # create an instance of the model with the data provided in the form
        new_employee = Employee(employeeid=employeeid, firstname=firstname, lastname=lastname, gender=gender, dob=dob,
                                address=address, mobile=mobile, emailid=emailid, department=department,
                                salary=salary, username=username, password=password)
  # save the new employee to the database
        new_employee.save()

        # redirect to a new page to show a success message
        return redirect('opt')
    else:
        return render(request, 'signup.html')

def logdoc(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request,'signin.html')



def unapproved_employees(request):
    unapproved_employees = Employee.objects.filter(is_approve=False)
    return render(request, 'unapproved_employees.html', {'unapproved_employees': unapproved_employees})

def approve_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.is_approve = True
    employee.save()
    return redirect('unapproved_employees')

def emplog(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request,'employeelogin.html')




def employee_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check if the provided credentials are valid
        try:
            employee = Employee.objects.get(username=username, password=password, is_approve=True)
        except Employee.DoesNotExist:
            messages.error(request, 'Invalid username or password.')
            return redirect('emplog')

        # Perform any additional actions for a successful login if needed

        return redirect('emp_dashboard')  # Replace 'dashboard' with the actual URL you want to redirect to after login

    return render(request, 'employeelogin.html')  # Replace 'employee_login.html' with the actualtemplatename

def emp_dashboard(request):
    return render(request,'emp_dashboard.html')


def atten(request):
    return render(request,'attandance.html')

def leave(request):
    return render(request,'leavereq.html')

def emplogout(request):
    return render(request,'options.html')

def leave_request(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        leave_type = request.POST['leave_type']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        reason = request.POST['reason']

        new_leave=LeaveApplication(Name=Name,leave_type=leave_type, start_date=start_date, end_date=end_date, reason=reason )
        new_leave.save()
        return redirect('emp_dashboard')
    else:
        return render(request, 'leavereq.html')


def leave_request_list(request):
    leave_requests = LeaveApplication.objects.all()
    return render(request, 'leavereport.html', {'leave_requests': leave_requests})

def approve_leave(request):
    le=LeaveApplication.objects.all()
    le.is_approve = True


    return redirect('admin_dashboard')



def leave_request(request):
    if request.method == 'POST':
        Name = request.POST['Name']

        new_leave=LeaveApplication(Name=Name,leave_type=leave_type, start_date=start_date, end_date=end_date, reason=reason )
        new_leave.save()
        return redirect('emp_dashboard')
    else:
        return render(request, 'leavereq.html')
