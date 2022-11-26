import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from scores.models import Student


@csrf_exempt
def register(request):
    if request.method == 'POST':
        s = json.loads(request.body)
        uuid = s['le_cookie']
        fname = s['fname']
        lname = s['lname']
        sex = s['sex']
        ethnicity = s['ethnicity']
        uni = s['uni']
        grad_date = s['grad_date']
        Student.objects.create(uuid=uuid, fname=fname, lname=lname, sex=sex, ethnicity=ethnicity, uni=uni, grad_date=grad_date)

    return None


@csrf_exempt
def submit(request):
    if request.method == 'POST':
        s = json.loads(request.body)
        uuid = s['le_cookie']
        points = int(s['ans'])
        student = Student.objects.get(uuid=uuid)
        student.points += points
        student.save()
    return None


def index(request):
    return render(request, 'index.html')
