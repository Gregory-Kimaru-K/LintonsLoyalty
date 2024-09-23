from django.shortcuts import render
from .models import Loyalcustomers
from django.http import JsonResponse
import re

# Create your views here.
def signup_view(request):
    return render(request, 'signup/signup.html')

def sign_up_cust(request):
    if request.method == 'POST':
        name = request.POST.get('customername')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        byear = request.POST.get('byear')
        bmonth = request.POST.get('bmonth')
        bday = request.POST.get('bday')

        if re.match(r'^07\d{8}$', phone):
            phone = '254' + phone[1:]

        elif re.match(r'^\+2547\d{8}$', phone):
            phone = phone[1:]

        elif re.match(r'^7\d{8}$', phone):
            phone = '254' + phone

        elif re.match(r'^011\d{7}$', phone):
            phone = '254' + phone[1:]

        elif re.match(r'^\+25411\d{7}$', phone):
            phone = phone[1:]

        elif re.match(r'^11\d{7}$', phone):
            phone = '254' + phone

        elif re.match(r'^254\d{9}$', phone):
            pass

        else:
            return JsonResponse({'msg' : "Invalid phone number format."})
        
        
        if Loyalcustomers.objects.filter(phone=phone).exists():
            return JsonResponse({'msg' : 'User with this number exists.'})
        
        return JsonResponse({'msg' : 'Type shit!'})