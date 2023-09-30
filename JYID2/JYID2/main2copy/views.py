import json
import string
from datetime import datetime
import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Person, Subject
from django.db import connection
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt


def mycapcha():
    realcap = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=6))
    return realcap


def index(request):
    return render(request, 'main/index.html')


def potom(request):
    jsoncome = request.body
    json_data = json.loads(jsoncome)
    json_data['datetime_field'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    json_data = json.dumps(json_data)
    return HttpResponse(json_data)


def setget(request):
    jsoncome1 = json.loads(request.body)
    cap = jsoncome1['captcha']
    realcap = request.session['realcap']
    if cap == realcap:
        person = Person(
            name=jsoncome1['firstname'],
            last_name=jsoncome1['lastname'],
            age=jsoncome1['age'],
            email=jsoncome1['email']
        )
        person.save()
        arr = jsoncome1['state']
        for i in range(len(arr)):
            subject = Subject(person=person, name2=arr[i])
            subject.save()
        return HttpResponse(jsoncome1)
    elif cap != realcap:
        return HttpResponse('читать научись')


def get_subjects(request):
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM main_sub")
    rows = cursor.fetchall()
    subjects = [row[0] for row in rows]
    return JsonResponse(subjects, safe=False)


def get_mycaptca(request):
    captcha = mycapcha()
    request.session['realcap'] = captcha
    return JsonResponse(captcha, safe=False)

@csrf_exempt
def delete_record(request, id):
    try:
        record = Person.objects.get(id=id)
        record.delete()
        return JsonResponse({'success': True})
    except YourModel.DoesNotExist:
        return JsonResponse({'success': False}, status=404)

def edit(request, id):
    if request.method == 'GET':
        instance = get_object_or_404(Person, id=id)
        data = {
            'id': instance.id,
            'name': instance.name,
            'last_name': instance.last_name,
            'email': instance.email,
            'age': instance.age,
        }
        return JsonResponse(data)


def update(request, id):
    if request.method == 'POST':
        instance = get_object_or_404(Person, id=id)
        instance.name = request.POST['name']
        instance.last_name = request.POST['last_name']
        instance.email = request.POST['email']
        instance.age = request.POST['age']
        instance.save()
        return JsonResponse({'message': 'Изменения успешно сохранены'})
