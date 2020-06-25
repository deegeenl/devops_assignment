import datetime
import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from person.models import Person


class ApiView(View):

    def get(self, request, name):
        p = get_object_or_404(Person, name=name)
        message = f"Hello, {name.title()}!"
        days = p.days_till_birthday()
        greeting = "Happy Birthday!" if days == 0 else f"Your birthday is in {days} days."
        return JsonResponse({'message': message + " " + greeting})

    @csrf_exempt
    def put(self, request, name):
        try:
            data = json.loads(request.body)
            dob = data.get('dateOfBirth')
        except json.decoder.JSONDecodeError:
            return JsonResponse({'error': "Malformed JSON provided"}, status=401)

        if not dob:
            return JsonResponse({'error': "No date of birth provided"}, status=401)

        try:
            dob = datetime.date.fromisoformat(dob)
        except ValueError:
            return JsonResponse({'error': "Date format isn't ISO, should be YYYY-MM-DD"}, status=401)

        Person.objects.update_or_create(name=name, defaults={'dob': dob})
        return JsonResponse({}, status=204)

