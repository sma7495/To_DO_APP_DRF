from django.db import models
from account.models import Profile



class Project(models.Model):
    STATUS_CHOICES = [
    ('done', 'Done'),
    ('late', 'Be Late'),
    ('working', 'on working'),
    ('wait', 'wiating for start'),
    ]
    title = models.CharField(max_length=250)
    description = models.TextField()
    dead_time = models.DateTimeField()
    start_time = models.DateTimeField()
    spending_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='wait')
    priority = models.SmallIntegerField(default=100)
    related_user = models.ManyToManyField(to = Profile)
    manager = models.ForeignKey(to=Profile, on_delete= models.PROTECT, related_name='project_manager')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
class SubProject(models.Model):
    STATUS_CHOICES = [
    ('done', 'Done'),
    ('late', 'Be Late'),
    ('working', 'on working'),
    ('wait', 'wiating for start'),
    ]
    title = models.CharField(max_length=250)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    description = models.TextField()
    dead_time = models.DateTimeField()
    start_time = models.DateTimeField()
    spending_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='wait')
    priority = models.SmallIntegerField(default=100)
    related_user = models.ManyToManyField(to = Profile, related_name='sub_project_user')
    manager = models.ForeignKey(to=Profile, on_delete= models.PROTECT, related_name='sub_project_manager')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class Task(models.Model):
    STATUS_CHOICES = [
    ('done', 'Done'),
    ('late', 'Be Late'),
    ('working', 'on working'),
    ('wait', 'wiating for start'),
    ]
    title = models.CharField(max_length=250)
    sub_project = models.ForeignKey(to=SubProject, on_delete=models.CASCADE)
    description = models.TextField()
    dead_time = models.DateTimeField()
    start_time = models.DateTimeField()
    spending_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='wait')
    priority = models.SmallIntegerField(default=100)
    related_user = models.ManyToManyField(to = Profile, related_name='task_user')
    manager = models.ForeignKey(to=Profile, on_delete= models.PROTECT, related_name='task_manager')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
