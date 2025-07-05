from django.test import TestCase
from django.contrib.auth import get_user_model

from ..models import Task, SubProject, Project
from account.models import Profile


User = get_user_model()


class TestTaskModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@ex.com", password="string1234")

        profile = Profile.objects.get(user=self.user)
        self.profile = profile

        proj = Project(
            title="proj1",
            description="test des",
            dead_time="2025-08-05T15:05:31.538Z",
            start_time="2025-07-05T15:05:31.538Z",
            spending_time=0,
            status="done",
            priority=1,
            manager=profile,
        )
        proj.save()

        sub_proj = SubProject(
            title="sub_proj_1",
            project=proj,
            description="test des",
            dead_time="2025-08-05T15:05:31.538Z",
            start_time="2025-07-05T15:05:31.538Z",
            spending_time=0,
            status="done",
            priority=1,
            manager=profile,
        )
        sub_proj.save()

        sub_proj2 = SubProject(
            title="sub_proj_2",
            project=proj,
            description="test des",
            dead_time="2025-08-05T15:05:31.538Z",
            start_time="2025-07-05T15:05:31.538Z",
            spending_time=0,
            status="done",
            priority=1,
            manager=profile,
        )
        sub_proj2.save()

        task = Task(
            title="task1",
            sub_project=sub_proj,
            description="test des",
            dead_time="2025-08-05T15:05:31.538Z",
            start_time="2025-07-05T15:05:31.538Z",
            spending_time=0,
            status="done",
            priority=1,
            manager=profile,
        )
        task.save()

        task2 = Task(
            title="task2",
            sub_project=sub_proj,
            description="test des",
            dead_time="2025-08-05T15:05:31.538Z",
            start_time="2025-07-05T15:05:31.538Z",
            spending_time=0,
            status="done",
            priority=1,
            manager=profile,
        )
        task2.save()

        task3 = Task(
            title="task3",
            sub_project=sub_proj,
            description="test des",
            dead_time="2025-08-05T15:05:31.538Z",
            start_time="2025-07-05T15:05:31.538Z",
            spending_time=0,
            status="done",
            priority=1,
            manager=profile,
        )
        task3.save()

        self.task = task
        self.task2 = task2
        self.task3 = task3
        self.sub_proj = sub_proj
        self.sub_proj2 = sub_proj2
        self.proj = proj

    def test_profile_post_seve(self):
        profile = self.profile
        self.assertTrue(Profile.objects.filter(id=profile.id).exists())

    def test_create_task_models(self):

        self.assertTrue(Task.objects.filter(id=self.task.id).exists())
        self.assertTrue(Task.objects.filter(id=self.task2.id).exists())
        self.assertTrue(Task.objects.filter(id=self.task3.id).exists())

        self.assertTrue(SubProject.objects.filter(id=self.sub_proj.id).exists())
        self.assertTrue(SubProject.objects.filter(id=self.sub_proj2.id).exists())

        self.assertTrue(Project.objects.filter(id=self.proj.id).exists())

    def test_task_late_status(self):
        task = self.task
        task2 = self.task2
        task3 = self.task3

        task.status = "done"
        task.save()

        task2.status = "working"
        task2.save()

        task3.status = "late"
        task3.save()
        sub_proj = SubProject.objects.get(id=1)
        proj = Project.objects.get(id=1)

        self.assertEqual(sub_proj.status, "late")
        self.assertEqual(proj.status, "late")

    def test_task_working_status(self):
        task = self.task
        task2 = self.task2
        task3 = self.task3

        task.status = "done"
        task.save()

        task2.status = "working"
        task2.save()

        task3.status = "done"
        task3.save()

        sub_proj = SubProject.objects.get(id=1)
        proj = Project.objects.get(id=1)

        self.assertEqual(sub_proj.status, "working")
        self.assertEqual(proj.status, "working")

    def test_task_working_status2(self):
        task = self.task
        task2 = self.task2
        task3 = self.task3

        task.status = "done"
        task.save()

        task2.status = "working"
        task2.save()

        task3.status = "wait"
        task3.save()

        sub_proj = SubProject.objects.get(id=1)
        proj = Project.objects.get(id=1)

        self.assertEqual(sub_proj.status, "working")
        self.assertEqual(proj.status, "working")

    def test_task_wait_status(self):
        task = self.task
        task2 = self.task2
        task3 = self.task3

        task.status = "done"
        task.save()

        task2.status = "wait"
        task2.save()

        task3.status = "done"
        task3.save()

        sub_proj = SubProject.objects.get(id=1)
        proj = Project.objects.get(id=1)

        self.assertEqual(sub_proj.status, "wait")
        self.assertEqual(proj.status, "wait")

    def test_task_done_status(self):
        task = self.task
        task2 = self.task2
        task3 = self.task3

        task.status = "done"
        task.save()

        task2.status = "done"
        task2.save()

        task3.status = "done"
        task3.save()

        sub_proj = SubProject.objects.get(id=1)
        proj = Project.objects.get(id=1)

        self.assertEqual(sub_proj.status, "done")
        self.assertEqual(proj.status, "done")

    def test_task_spending_time(self):
        task = self.task
        task2 = self.task2
        task3 = self.task3

        task.spending_time = 8
        task.save()

        task2.spending_time = 12
        task2.save()

        task3.spending_time = 3
        task3.save()

        sub_proj2 = self.sub_proj2
        sub_proj2.spending_time = 5
        sub_proj2.save()

        sub_proj = SubProject.objects.get(id=1)
        proj = Project.objects.get(id=1)

        self.assertEqual(sub_proj.spending_time, 23)
        self.assertEqual(proj.spending_time, 28)
