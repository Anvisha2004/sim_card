from django.shortcuts import render
import mysql.connector

fn = ''
ln = ''
sm = ''
ph = ''
st = ''
act = ''

def useraction(request):
    if request.method == 'POST':
        m = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="", 
            database="sim" 
        )
        cursor = m.cursor()
        d = request.POST
        fn = d.get("first_name")
        ln = d.get("last_name")
        sm = d.get("sim_number")
        ph = d.get("phone_number")
        st = d.get("status")
        act = d.get("activation_date")
        query = "INSERT INTO user (first_name, last_name, sim_number, phone_number, status, activation_date) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (fn, ln, sm, ph, st, act))
        
        m.commit()

        cursor.close()
        m.close()

    
        return render(request, 'user_input.html')

    return render(request, 'user_input.html')
from django.http import JsonResponse
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework import statuss

from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import User  
from django.utils import timezone
from rest_framework import status


def activate_sim_page(request):
    return render(request, 'activate_sim.html')

def deactivate_sim_page(request):
    return render(request, 'deactivate_sim.html')

def get_sim_details_page(request):
    return render(request, 'get_sim_details.html')

@api_view(['POST'])
def activate_user(request):
    sim_number = request.data.get('sim_number')  # Assuming sim_number is still the field to activate
    try:
        user = User.objects.get(sim_number=sim_number)  # Adjusted to use User model
        if user.status == 'inactive':
            user.status = 'active'
            user.activation_date = timezone.now()
            user.save()
            return JsonResponse({'message': 'User activated successfully!'}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'message': 'User is already active.'}, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def deactivate_user(request):
    sim_number = request.data.get('sim_number')
    try:
        user = User.objects.get(sim_number=sim_number)
        if user.status == 'active':
            user.status = 'inactive'
            user.save()
            return JsonResponse({'message': 'User deactivated successfully!'}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'message': 'User is already inactive.'}, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_user_details(request, sim_number):
    try:
        user = User.objects.get(sim_number=sim_number)
        user_data = {
            'sim_number': user.sim_number,
            'status': user.status,
            'activation_date': user.activation_date,
        }
        return JsonResponse(user_data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
