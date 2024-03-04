from django import forms
from .models import JobDetails

class JobDetailsForm(forms.ModelForm):
    class Meta:
        model = JobDetails
        fields = ['jobtitle', 'jobfile']
    

