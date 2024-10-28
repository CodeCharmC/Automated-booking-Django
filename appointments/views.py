from django.http import JsonResponse
from .models import Appointment
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def create_appointment(request):
   if request.method == 'POST':
      data = json.loads(request.body)
      appointment = Appointment.objects.create(**data)
      return JsonResponse({"id": appointment.id, "status": "Created"}, status=201)

@csrf_exempt
def get_appointments(request):
   appointments = list(Appointment.objects.values())
   return JsonResponse(appointments, safe=False)

@csrf_exempt
def update_appointment(request, id):
   data = json.loads(request.body)
   Appointment.objects.filter(id=id).update(**data)
   return JsonResponse({"status": "Updated"}, status=200)

@csrf_exempt
def delete_appointment(request, id):
   Appointment.objects.filter(id=id).delete()
   return JsonResponse({"status": "Deleted"}, status=204)
