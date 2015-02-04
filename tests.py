from django.core.urlresolvers import reverse
from todo.models import Task
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.forms.models import model_to_dict
import json

# Create your tests here.


def create_task_mock(name):
        url = reverse('todo:list')
        model = Task(name=name)
        result = model_to_dict(model)
        client = APIClient()
        response = client.post(url, data=result, format="json")
        return response


class RestAPITest(APITestCase):

    def to_json(self, data):
        return json.loads(data)

    """
    Get Tasks when there is no tasks.
    """
    def test_list_get_no_tasks(self):
        url = reverse('todo:list')
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertQuerysetEqual(self.to_json(response.content),
                                 self.to_json("[]"))

    """
    Create a task.
    """
    def test_create_task(self):
        name = "Foo"
        response = create_task_mock(name)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, name)

    """
    Get a task.
    """
    def test_list_get(self):
        name = "Foo"
        create_task_mock(name)

        url = reverse('todo:list')
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, name)

    """
    Get the test task
    """
    def test_detail_get(self):
        name = "Foo"
        create_task_mock(name)

        url = '/todo/1/'
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, name)

    def test_detail_update(self):
        name = "Foo"
        create_task_mock(name)

        name = "Bar"
        model = Task(name=name)
        result = model_to_dict(model)

        url = '/todo/1/'
        response = self.client.put(url, data=result, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, name)

    def test_detail_delete(self):
        name = "Foo"
        create_task_mock(name)

        url = '/todo/1/'
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
