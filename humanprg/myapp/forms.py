from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from .models import LeaveApplication

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

from django import forms

class LeaveRequestApprovalForm(forms.Form):
    # You can include fields if needed for approval/rejection comments, etc.
    pass  # No additional fields requiredinthisexample


