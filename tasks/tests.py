from django.test import TestCase
from django.urls import reverse

from .models import Task


class TaskViewsTests(TestCase):
    def test_empty_list_message_is_displayed(self):
        response = self.client.get(reverse("task_list"))
        self.assertContains(response, "No tasks available")

    def test_task_can_be_created_updated_toggled_and_deleted(self):
        self.client.post(reverse("add_task"), {"title": "Study Django", "description": "Practice CRUD", "completed": False})
        task = Task.objects.get(title="Study Django")
        self.client.post(reverse("edit_task", args=[task.pk]), {"title": "Study Django", "description": "Practice forms", "completed": False})
        task.refresh_from_db()
        self.assertEqual(task.description, "Practice forms")
        self.client.post(reverse("toggle_task_status", args=[task.pk]))
        task.refresh_from_db()
        self.assertTrue(task.completed)
        self.client.post(reverse("delete_task", args=[task.pk]))
        self.assertFalse(Task.objects.exists())
