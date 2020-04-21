from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import get_user_model


def index(request):
    all_users= get_user_model().objects.all()
    return render(request, 'index.html', {'all_users': all_users})