from django.shortcuts import render
from django.http import HttpResponse
from stellarapp.models import Orders

# Create your views here.
def index(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def requestpage(request):
    return render(request, 'Requestpage.html')

def request_submitted(request):
    name = request.POST['name']
    email = request.POST['email']
    address = request.POST['address']
    category = request.POST['category']
    timeslot = request.POST['timeslot']

    orders = Orders(name=name, email=email, address=address, category=category, timeslot=timeslot)
    orders.save()
    return render(request, 'success.html')
