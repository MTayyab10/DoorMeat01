from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from orders3.models import Customer


def index(request):

    # messages.info(request, "10% off on this Eid")

    customers = Customer.objects.all()

    # customer for checking is it have orders or not
    # in Customer Model, MyOrder
    customer_orders = Customer.objects.filter(name=request.user.username).count()

    # just print in terminal
    print(request.user.username, "have total orders", customer_orders)

    # Offer like 20% Off

    offer = True
    offer_text = ''
    if offer:
        offer_text = "20% Off, Hurry Up book Butcher now!"

    return render(request, 'home1/index.html', {
        'customers': customers,
        'customer_orders': customer_orders,
        'offer': offer,
        'offer_text': offer_text
    })


def about(request):
    return render(request, 'home1/about.html')


def contact(request):
    if request.method == 'POST':
        username = request.POST['username']
        mobile = request.POST['mobile']
        email = request.POST['email']
        message = request.POST['message']

        c = Contact(username=username, mobile=mobile,
                    email=email, message=message)
        c.save()
        print("Message Received")
        messages.success(request, "Submitted Successfully")
        return redirect('home1:contact')

    return render(request, 'home1/contact.html')
