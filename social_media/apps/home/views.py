from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse


def index(requst):
    return render(requst, 'index.html')