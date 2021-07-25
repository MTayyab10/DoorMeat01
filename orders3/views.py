from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect, reverse
from django.utils.timezone import datetime

from .forms import (
    CustomerChangeForm, ButcherChangeForm
)
from .models import Customer, Butcher


# CUSTOMER SECTION

def customer_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobile = request.POST['mobile']
        town = request.POST['town']
        city = request.POST['city']
        animal = request.POST['animal']
        quantity = request.POST['quantity']
        time = request.POST['time']
        heard = request.POST['heard']
        # date_order = request.POST['date']

        # coupon = request.POST['coupon']

        c = Customer(name=name, mobile=mobile, town=town, city=city, quantity=quantity,
                     time=time, animal=animal, heard=heard)
        c.save()

        # if coupon is not None:
        #     cpn = Customer(coupon=coupon)
        #     cpn.save()
        #     print('coupon got it')
        # else:
        #     print('coupon do not have3 ')

        print("Customer Form Received")

        # messages.info(request, "Your form is received")

        url = reverse('orders3:cust_response', args=(c.id,))
        return HttpResponseRedirect(url)

    # specific customer
    one_customer = Customer.objects.filter(name=request.user.username)

    # total or all customers in Customer model
    customers = Customer.objects.all()

    # count/total customers
    count_customers = Customer.objects.count()
    # for c in customers:
    #     print(c.animal.count() > 1)

    # check - if user is already fill Butcher form
    check_butcher = Butcher.objects.filter(name=request.user.username).exists()

    # date time
    date = datetime.today()
    print(date)

    return render(request, 'orders3/customer_form.html', {
        'one_customer': one_customer,
        'customers': customers,
        'count_customers': count_customers,
        'check_butcher': check_butcher,
        # 'date': date,

    })


def cust_response(request, customer_id):
    # customer = Customer.objects.get(pk=customer_id)
    customer = get_object_or_404(Customer, pk=customer_id)

    price = 0
    price_before_qty = 0
    service_fee = 0
    total = 0

    # quantity of orders
    qty = float(customer.quantity)  # float
    qty1 = customer.quantity  # int

    # check animals

    goat = customer.animal == 'Goat/sheep (bakra, etc)'
    cow = customer.animal == 'Cow/buffalo (gai)'
    camel = customer.animal == 'Camel (ont)'

    # city
    lhr = customer.city == 'Lahore'

    # coupon_valid = ''
    # coupon_valid = Discount.objects.get(cpn_id=customer.id)

    # coupon = False
    # if coupon_valid.coupon == 'abd':
    #     coupon = True
    #     print('coupon in cust_response')
    #
    # print(Discount.cpn_id.pk)

    # coupon_valid = Discount.objects.get(cpn_id_id=customer.id)
    if goat:
        if lhr:

            service_fee = 750.00
            price_before_qty = 1500
            price = price_before_qty * qty
        else:
            service_fee = 500.00
            price_before_qty = 1300.00
            price = price_before_qty * qty  # number of ani

        total = price + (service_fee * qty)  # s_fee will also multiply

    elif cow:
        if lhr:
            service_fee = 1150.00
            price_before_qty = 15000.00
            price = price_before_qty * qty

        else:
            service_fee = 800.00
            price_before_qty = 13000.00
            price = price_before_qty * qty

        total = price + (service_fee * qty)

    elif camel:

        if lhr:
            service_fee = 1850.00
            price_before_qty = 20000.00
            price = price_before_qty * qty
        else:
            service_fee = 1350.00
            price_before_qty = 18000.00
            price = price_before_qty * qty

        total = price + (service_fee * qty)

    return render(request, 'orders3/cust_response.html', {
        'customer': customer,

        'price': price, 'price_before_qty': price_before_qty,
        'service_fee': service_fee,
        'total': total,
        'qty': qty, 'qty1': qty1,
        # 'coupon_valid': coupon_valid,
        # 'coupon': coupon
    })


# def cust_coupon(request, customer_id):
#     customer = get_object_or_404(Customer, pk=customer_id)
#
#     discount = Discount.objects.get(pk=customer.id)
#     coupon = discount.coupon
#     print(coupon)
#     # customer = Customer.objects.get(pk=)
#
#     if request.method == 'POST':
#         coupon = request.POST['coupon']
#         # cpn_id = request.POST['cpn_id']
#
#         c = Discount(coupon=coupon)
#         # d = Discount.objects.create()
#         c.save()
#         print('Coupon is save now')
#
#         messages.success(request, 'Fucking coupon code')
#
#         # url = reverse('orders3:cust_response', args=(customer.id,))
#         # return HttpResponseRedirect(url)
#         return HttpResponse('Yeah dsjkhfsaihdh')
#
#     else:
#         print('Sth is wrong with it')
#
#     return render(request, 'orders3/customer_form.html', {
#         'customer': customer,
#         'coupon': coupon,
#         # '# 'coupon_valid': coupon_valid,
#     })


# def cust_coupon_update(request, customer_id):
#     customer = Customer.objects.get(pk=customer_id)
#
#     if request.method == "POST":
#         form = DiscountChangeForm(request.POST, instance=customer)
#         if form.is_valid():
#             form.save()
#             print('Discount Coupon has changed')
#
#             messages.success(request, 'Your Order info is updated')
#
#             url = reverse('orders3:cust_response', args=(customer.id,))
#             return HttpResponseRedirect(url)
#
#             # return render(request, 'orders3/customer_form.html', {'url': url})
#         else:
#             form = CustomerChangeForm(instance=customer)
#     else:
#         form = CustomerChangeForm(instance=customer)
#
#     return render(request, "orders3/cust_order_update.html", {
#         'form': form,
#         'customer': customer
#     })


def cust_order_update(request, customer_id):
    order = Customer.objects.get(pk=customer_id)

    if request.method == 'POST':
        form = CustomerChangeForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            print("Customer Form Updated")

            messages.success(request, 'Your Order info is updated')

            url = reverse('orders3:cust_response', args=(order.id,))
            return HttpResponseRedirect(url)

            # return render(request, 'orders3/customer_form.html', {'url': url})
        else:
            form = CustomerChangeForm(instance=order)
    else:
        form = CustomerChangeForm(instance=order)

    return render(request, "orders3/cust_order_update.html", {
        'form': form,
        'order': order
    })


def cust_order_confirm(request, customer_id):
    order = Customer.objects.get(pk=customer_id)
    return render(request, 'orders3/cust_response.html', {
        'order': order
    })


def cust_order_delete(request, customer_id):
    order = Customer.objects.get(pk=customer_id)
    order.delete()

    return redirect('orders3:customer_form')


# BUTCHER SECTION

def butcher_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        # img = request.POST['img']
        mobile = request.POST['mobile']
        city = request.POST['city']
        town = request.POST['town']
        experience = request.POST['experience']
        speciality = request.POST['speciality']
        time = request.POST['time']
        price = request.POST['price']
        heard = request.POST['heard']

        b = Butcher(name=name, mobile=mobile,
                    city=city, town=town, experience=experience,
                    speciality=speciality, time=time,
                    price=price, heard=heard)
        b.save()

        print("Butcher form received")

        url = reverse('orders3:butch_response', args=(b.id,))
        return HttpResponseRedirect(url)

    # specific customer
    one_butcher = Butcher.objects.filter(name=request.user.username)

    # count total orders
    all_butchers = Customer.objects.count()

    # check user is exist or not in Customer
    check_customer = Customer.objects.filter(name=request.user.username).exists()

    return render(request, 'orders3/butcher_form.html', {
        'one_butcher': one_butcher,
        'all_butchers': all_butchers,
        'check_customer': check_customer
    })


def butch_response(request, butcher_id):
    butcher = Butcher.objects.get(pk=butcher_id)

    return render(request, 'orders3/butch_response.html', {
        'butcher': butcher
    })


def butch_order_update(request, butcher_id):
    order = Butcher.objects.get(pk=butcher_id)

    if request.method == 'POST':
        form = ButcherChangeForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            print("Butcher form Updated")

            url = reverse('orders3:butch_response', args=(order.id,))
            return HttpResponseRedirect(url)

        else:
            form = ButcherChangeForm(instance=order)
    else:
        form = ButcherChangeForm(instance=order)

    return render(request, "orders3/butch_order_update.html", {
        'form': form,
        'order': order
    })


def butch_order_delete(request, butcher_id):
    order = Butcher.objects.get(pk=butcher_id)
    order.delete()
    return redirect('orders3:butcher_form')


# Just Order Info Contain Few Bugs

def order_info(request, user_id):
    user = Customer.objects.get(pk=user_id)
    # butcher = Butcher.objects.get(pk=user_id)
    return render(request, 'accounts2/edit_profile.html', {
        'user': user,
        # 'butcher': butcher,
    })


# HELP / SUPPORT

def support(request):
    return render(request, 'orders3/help.html')
