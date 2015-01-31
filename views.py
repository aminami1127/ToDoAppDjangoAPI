from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-

import json
from collections import OrderedDict
from django.http import HttpResponse
from todo.models import Task
from api.serializers import TaskSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

def list(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    context = JSONRenderer().render(serializer.data)
    return HttpResponse(context, content_type='application/json; charset="utf-8"')
