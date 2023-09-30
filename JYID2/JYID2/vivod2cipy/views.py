import json
import random
import string
from django.db import connection
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from main.models import Person, Subject
from django.db.models import Q
import time


def main(request):
    return render(request, 'vivod/index.html')


def datatable_data(request):
    draw = int(request.GET.get('draw', 0))
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    search_value = request.GET.get('search[value]', '')
    order_column = request.GET.get('order[0][column]')
    order_dir = request.GET.get('order[0][dir]')

    column_names = [
        'id', 'name', 'last_name', 'email', 'age'
    ]

    order_column_name = column_names[int(order_column)]
    if order_dir == 'desc':
        order_column_name = '-' + order_column_name

    queryset = Person.objects.filter(
        Q(name__icontains=search_value) |
        Q(last_name__icontains=search_value) |
        Q(email__icontains=search_value) |
        Q(age__icontains=search_value)
    ).order_by(order_column_name)

    total_records = queryset.count()

    # if total_records == 0:
    #     empty_data = [{'id': None, 'name': "", 'second_name': "", 'email': "", 'age': ""}] * length
    #     data = empty_data[start:start + length]
    # else:

    queryset = queryset[start:start + length]
    data = []
    for person in queryset:
        data.append({
            'id': person.id,
            'name': person.name,
            'last_name': person.last_name,
            'email': person.email,
            'age': person.age
        })

    response = {
        'draw': draw,
        'recordsTotal': total_records,
        'recordsFiltered': total_records,
        'data': data
    }
    time.sleep(0)
    return JsonResponse(response)


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


def mycapcha():
    realcap = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=6))
    return realcap


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
