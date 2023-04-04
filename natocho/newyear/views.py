from django.shortcuts import render

import datetime

from django.http import HttpResponse

# Create your views here.
def test(request):
    now = datetime.datetime.now
    return render(request,"index1.html")