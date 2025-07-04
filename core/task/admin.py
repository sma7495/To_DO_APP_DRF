from django.contrib import admin
from .models import Project, SubProject, Task

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "manager")
    list_filter = ("status","related_user")
    search_fields = ["title", "description"]
    summernote_fields = ("description",)

class SubProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "manager", "project")
    list_filter = ("status","related_user")
    search_fields = ["title", "description"]
    summernote_fields = ("description",)
    

class TaskAdmin(admin.ModelAdmin):
    list_display = ("id","title", "status", "manager", "sub_project")
    list_filter = ("status","related_user")
    search_fields = ["title", "description"]
    summernote_fields = ("description",)



admin.site.register(Project, ProjectAdmin)

admin.site.register(SubProject, SubProjectAdmin)

admin.site.register(Task, TaskAdmin)