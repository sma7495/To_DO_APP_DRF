from django.urls import path

from .views import (
    TaskModelViewSet,
    SubProjectModelViewSet,
    ProjectModelViewSet,
)


app_name = "api"

urlpatterns = [
    path(
        "task_list/",
        TaskModelViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="task_list",
    ),
    path(
        "task_detail/<int:pk>",
        TaskModelViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "delete": "destroy",
            }
        ),
        name="task_detail",
    ),
    # For Sub Projects:
    path(
        "sub_project_list/",
        SubProjectModelViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="sub_project_list",
    ),
    path(
        "sub_project_detail/<int:pk>",
        SubProjectModelViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "delete": "destroy",
            }
        ),
        name="sub_project_detail",
    ),
    # For Sub Projects:
    path(
        "project_list/",
        ProjectModelViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="project_list",
    ),
    path(
        "project_detail/<int:pk>",
        ProjectModelViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "delete": "destroy",
            }
        ),
        name="project_detail",
    ),
]
