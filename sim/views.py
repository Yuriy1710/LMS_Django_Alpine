from datetime import datetime

from typing import AsyncGenerator
from django.shortcuts import render, redirect
from django.http import HttpRequest, StreamingHttpResponse, HttpResponse
from . import models
import json
import random


def lobby(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get('username')
        return redirect('chat')