from django.shortcuts import render
from .models import Loyalcustomers
from django.http import JsonResponse


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


        print(phone)
        
        if Loyalcustomers.objects.filter(phone=phone).exists():
            return JsonResponse({'msg' : 'User with this number exists.'})
        