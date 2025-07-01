from rest_framework.viewsets import ModelViewSet
from rest_framework.views import Response

from .serializers import TaskSerializer, SubProjectSerializer, ProjectSerializer
from ...models import Task, SubProject, Project
from .pagination import TaskPaginations

class TaskModelViewSet(ModelViewSet):
    pagination_class = TaskPaginations
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    

class SubProjectModelViewSet(ModelViewSet):
    pagination_class = TaskPaginations
    serializer_class = SubProjectSerializer
    queryset = SubProject.objects.all()


class ProjectModelViewSet(ModelViewSet):
    pagination_class = TaskPaginations
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()