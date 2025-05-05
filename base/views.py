import json

from django.http import HttpResponse
from django.shortcuts import render
from .forms import InsuranceForm


# Create your views here.

def home(request):
    if request.method == "POST":
        form = InsuranceForm(request.POST)
        if form.is_valid():
            return result(request)
    else:
        form = InsuranceForm()

    return render(request, 'base/home.html', {"form": form})


def result(request):
    form = InsuranceForm(request.POST)
    result = "0"
    if form.is_valid():
        return render(request, 'base/result.html', {"result": result})

    context = {
        'status': '400', 'reason': 'Bad Request',
    }
    response = HttpResponse(json.dumps(context), content_type='application/json')
    response.status_code = 400
    return response
