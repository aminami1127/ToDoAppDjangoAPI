# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from todo.models import Task
from todo.serializers import TaskSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

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
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        return JSONRespose(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer  = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONRespose(serializer.data, status=201)
        return JSONRespose(serializer.errors, status=400)

@csrf_exempt
def detail(request, pk):
    """
    Retrieve, update or delete a Task
    """
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=400)

    if request.method == 'GET':
        serializer =  TaskSerializer(task)
        return JSONRespose(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(task, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONRespose(serializer.data)
        return JSONRespose(serializer.errors, status=400)

    elif request.method == 'DELETE':
        task.delete()
        return HttpResponse(status=204)
