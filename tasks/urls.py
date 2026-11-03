from django.urls import path

from . import views

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("tasks/add/", views.add_task, name="add_task"),
    path("tasks/<int:pk>/edit/", views.edit_task, name="edit_task"),
    path("tasks/<int:pk>/toggle/", views.toggle_task_status, name="toggle_task_status"),
    path("tasks/<int:pk>/delete/", views.delete_task, name="delete_task"),
]
