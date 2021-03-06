from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout


import os
import shutil
import json
import datetime
import signal
import random
import uuid


from scarf.settings import BASE_DIR
from sage.models import  *

from discs.settings import DATABASES_NAMES
from discs.services.underlying import databaseRead 


def home(request):
    # Hello this is a function which returns home
    return render(request, 'base.html', {
        'DATABASES_NAMES' : DATABASES_NAMES,
    })
    # return HttpResponse("Hello")

@csrf_exempt
def getUsers(request):
    if request.method == 'POST':
        dbName = json.loads(request.POST['dbName'])
        # print('dbName : ', dbName)
        users_json = databaseRead.readUsers(dbName=dbName).to_json()
        users = json.dumps(users_json)
        # print('type of users : ', type(users))
        return JsonResponse({
            "status" : True,
            "users" : users,
        })
    