# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from todo.models import Task
from todo.serializers import TaskSerializer
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


def index(request):
    return render(request, 'todo/index.html')

"""
return HttpResponse as JSON from its content
"""


def JSONRespose(data, **kwargs):
    content = JSONRenderer().render(data)
    kwargs['content_type'] = 'application/json; charset="utf-8"'
    return HttpResponse(content, kwargs)


@csrf_exempt
def list(request):
    """
    List all Tasks or create new one
    """
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return JSONRespose(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONRespose(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JSONRespose(serializer.errors,
                               status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def detail(request, pk):
    """
    Retrieve, update or delete a Task
    """
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return JSONRespose(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(task, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONRespose(serializer.data)
        return JSONRespose(serializer.errors,
                           status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
