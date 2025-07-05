from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from .serializers import (
    TaskSerializer,
    SubProjectSerializer,
    ProjectSerializer,
)
from ...models import Task, SubProject, Project
from .pagination import TaskPaginations
from .permissions import IsRelatedUserOrManager


class TaskModelViewSet(ModelViewSet):
    pagination_class = TaskPaginations
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated, IsRelatedUserOrManager]

    def get_queryset(self):
        query_set = super().get_queryset()
        query_set = query_set.filter(
            Q(related_user__user__id=self.request.user.id)
            | Q(manager__user__id=self.request.user.id)
        )
        return query_set


class SubProjectModelViewSet(ModelViewSet):
    pagination_class = TaskPaginations
    serializer_class = SubProjectSerializer
    queryset = SubProject.objects.all()
    permission_classes = [IsAuthenticated, IsRelatedUserOrManager]

    def get_queryset(self):
        query_set = super().get_queryset()
        query_set = query_set.filter(
            Q(related_user__user__id=self.request.user.id)
            | Q(manager__user__id=self.request.user.id)
        )
        return query_set


class ProjectModelViewSet(ModelViewSet):
    pagination_class = TaskPaginations
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated, IsRelatedUserOrManager]

    def get_queryset(self):
        query_set = super().get_queryset()
        query_set = query_set.filter(
            Q(related_user__user__id=self.request.user.id)
            | Q(manager__user__id=self.request.user.id)
        )
        return query_set
