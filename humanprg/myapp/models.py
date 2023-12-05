from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def _str_(self):
        return self.user.username


class Employee(models.Model):
    employeeid = models.IntegerField()
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    dob = models.DateField()
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=15)
    emailid = models.EmailField(max_length=100)
    department = models.CharField(max_length=100)
    salary = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    is_approve = models.BooleanField(default=False)

    def _str_(self):
        return self.name


from django.db import models


class Employeelist(models.Model):
    Name = models.CharField(max_length=100)
    is_approved = models.BooleanField(default=False)

    def _str_(self):
        return self.name



class LeaveApplication(models.Model):
    Name = models.CharField(max_length=20)
    leave_type = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    is_confirm = models.BooleanField(default=False)

    def _str_(self):
        return f"{self.Name} - {self.leave_type}"


