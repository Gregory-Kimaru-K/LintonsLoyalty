from django.shortcuts import render
from .models import Loyalcustomers
from django.http import JsonResponse
import re
from django.utils import timezone
import pytz
from datetime import timedelta

# Create your views here.
def signup_view(request):
    return render(request, 'signup/signup.html')

def sign_up_cust(request):
    if request.method == 'POST':
        name = request.POST.get('customername')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')

        byear = request.POST.get('byear') or None
        bmonth = request.POST.get('bmonth') or None
        bday = request.POST.get('bday') or None

        try:
            byear = int(byear) if byear else None
            bmonth = int(bmonth) if bmonth else None
            bday = int(bday) if bday else None
        except ValueError:
            return JsonResponse({'msg': 'Invalid birth date format.', 'success': 'False'})  

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
            return JsonResponse({'msg' : "Phone number format not supported.", 'success' : 'False'})
        
        if Loyalcustomers.objects.filter(phone=phone).exists():
            return JsonResponse({'msg' : 'User with this Phone Number exists.', 'success' : 'False'})
        
        else:
            timecreated = timezone.now()
            datecreated = timecreated + timedelta(hours=3)
            Loyalcustomers.objects.create(
                phone=phone,
                customername=name,
                gender=gender,
                email=email,
                datecreated=datecreated,
                points=100,
                lastupdated=datecreated,
                birth_year=byear,
                birth_month=bmonth,
                birth_day=bday
            )
            return JsonResponse({'msg' : f'{name} Type shit!', 'success' : 'True'})