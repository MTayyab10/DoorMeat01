from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from orders3.models import Customer


def index(request):

    # customer for checking is it have
    # in Customer form or not, MyOrder
    customer = Customer.objects.all()

    return render(request, 'home1/index.html', {
        'customer': customer
    })


def about(request):
    return render(request, 'home1/about.html')


def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        message = request.POST['message']

        c = Contact(first_name=first_name, last_name=last_name,
                    email=email, message=message)
        c.save()
        print("Message Received")
        messages.success(request, "Submitted Successfully")
        return redirect('home1:contact')

    return render(request, 'home1/contact.html')
