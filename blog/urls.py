from django.urls import path
from .views import projects, project, project_add, project_edit, project_delete,\
    search_result

urlpatterns = [
    path('', projects, name="projects"),
    path("search_result/", search_result, name="search_result_project"),
    path('project_add/', project_add, name="project_add"),
    path('project_edit/<uuid:id>/', project_edit, name="project_edit"),
    path('project_delete/<uuid:id>/', project_delete, name="project_delete"),
    path('<uuid:id>/', project, name="project")
    ]