from django.db import models

class HRInfo(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username

class JobDetails(models.Model):
    jobid = models.AutoField(primary_key=True)
    jobtitle = models.CharField(max_length=100)
    jobfile = models.FileField(upload_to='job_files/')
    hr_info = models.ForeignKey(HRInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.jobtitle
