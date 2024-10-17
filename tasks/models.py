from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True,null=True)
    due_date=models.DateField()
    complited=models.BooleanField(default=False)
    task_day=models.BooleanField(default=False)
    task_week=models.BooleanField(default=False)
    task_month=models.BooleanField(default=False)
    task_year=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title