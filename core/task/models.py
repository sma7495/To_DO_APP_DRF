from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from account.models import Profile


class Project(models.Model):
    STATUS_CHOICES = [
        ("done", "Done"),
        ("late", "Be Late"),
        ("working", "on working"),
        ("wait", "wiating for start"),
    ]
    title = models.CharField(max_length=250)
    description = models.TextField()
    dead_time = models.DateTimeField()
    start_time = models.DateTimeField()
    spending_time = models.IntegerField(default=0, help_text="minutes of Spending time")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="wait")
    priority = models.SmallIntegerField(default=100)
    related_user = models.ManyToManyField(to=Profile)
    manager = models.ForeignKey(
        to=Profile, on_delete=models.PROTECT, related_name="project_manager"
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_snipet_description(self):
        return self.description[0:50] + "..."


class SubProject(models.Model):
    STATUS_CHOICES = [
        ("done", "Done"),
        ("late", "Be Late"),
        ("working", "on working"),
        ("wait", "wiating for start"),
    ]
    title = models.CharField(max_length=250)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    description = models.TextField()
    dead_time = models.DateTimeField()
    start_time = models.DateTimeField()
    spending_time = models.IntegerField(default=0, help_text="minutes of Spending time")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="wait")
    priority = models.SmallIntegerField(default=100)
    related_user = models.ManyToManyField(to=Profile, related_name="sub_project_user")
    manager = models.ForeignKey(
        to=Profile,
        on_delete=models.PROTECT,
        related_name="sub_project_manager",
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_snipet_description(self):
        return self.description[0:50] + "..."


class Task(models.Model):
    STATUS_CHOICES = [
        ("done", "Done"),
        ("late", "Be Late"),
        ("working", "on working"),
        ("wait", "wiating for start"),
    ]
    title = models.CharField(max_length=250)
    sub_project = models.ForeignKey(to=SubProject, on_delete=models.CASCADE)
    description = models.TextField()
    dead_time = models.DateTimeField()
    start_time = models.DateTimeField()
    spending_time = models.IntegerField(default=0, help_text="minutes of Spending time")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="wait")
    priority = models.SmallIntegerField(default=100)
    related_user = models.ManyToManyField(to=Profile, related_name="task_user")
    manager = models.ForeignKey(
        to=Profile, on_delete=models.PROTECT, related_name="task_manager"
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_snipet_description(self):
        return self.description[0:50] + "..."


@receiver(post_save, sender=Task)
def change_sub_proj(sender, instance, created, **kwargs):
    sub_proj = SubProject.objects.get(id=instance.sub_project.id)
    related_tasks = Task.objects.filter(sub_project=sub_proj)
    spending_time = 0
    status = "done"
    for tsk in related_tasks:
        spending_time = spending_time + tsk.spending_time
        if tsk.status == "late":
            status = "late"
        elif tsk.status == "working" and status != "late":
            status = "working"
        elif tsk.status == "wait" and status != "working" and status != "late":
            status = "wait"
    sub_proj.status = status
    sub_proj.spending_time = spending_time
    sub_proj.save()


@receiver(post_save, sender=SubProject)
def change_proj(sender, instance, created, **kwargs):
    proj = Project.objects.get(title=instance.project.title)
    related_tasks = SubProject.objects.filter(project=proj)
    spending_time = 0
    status = "done"
    for tsk in related_tasks:
        spending_time = spending_time + tsk.spending_time
        if tsk.status == "late":
            status = "late"
        elif tsk.status == "working" and status != "late":
            status = "working"
        elif tsk.status == "wait" and status != "working" and status != "late":
            status = "wait"
    proj.status = status
    proj.spending_time = spending_time
    proj.save()
