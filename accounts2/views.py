from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User, auth
# for login after registeration
from django.contrib.auth import authenticate, login

from accounts2.forms import EditProfileForm

from orders3.models import Customer


def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        # mobile = request.POST['mobile']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username has taken already, try another")
                return redirect('accounts2:register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email has taken already, try another")
                return redirect('accounts2:register')

            else:
                user = User.objects.create_user(username=username, email=email, password=password1)

                # user do not need to login, after register
                user.save()
                # login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')

                # new_user = authenticate(request, username=username, password1=password1)
                # login(request, new_user)

                print('New User is Created')
                messages.success(request, 'Congrats, You are registered to DoorMeat')

                return redirect('home1:index')
        else:
            messages.info(request, "The password didn't matched")
            redirect('accounts2:register')
    else:
        return render(request, 'accounts2/register.html')

    return redirect('accounts2:register')


def signin(request):

    if request.method == 'POST':
        userinput = request.POST['username']
        password = request.POST['password']

    # User can login with name/email, iexact for case-sensitive
        try:
            username = User.objects.get(email__iexact=userinput).username
        except User.DoesNotExist:
            username = request.POST['username']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:

            # Redirect to previous page after login

            auth.login(request, user)

            print("User is login")
            messages.info(request, 'You are login to DoorMeat')

            # Redirect to previous page after login

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home1:index')

        else:
            messages.info(request, 'Invalid username or password')
            return redirect('accounts2:signin')

    else:
        return render(request, 'accounts2/signIn.html')


def logout(request):
    auth.logout(request)
    messages.info(request, 'You are logout from DoorMeat')
    return redirect('home1:index')


def edit_profile(request):

    # for showing to customer orderDetail
    customer = Customer.objects.all()

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EditProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "Update successful!", extra_tags='edit_profile')
                return redirect("accounts2:edit_profile")
            else:
                messages.error(request, "Invalid", extra_tags='edit_profile')
                return redirect("accounts2:edit_profile")

        else:
            form = EditProfileForm(instance=request.user)
            return render(request, "accounts2/edit_profile.html", {
                'form': form,
                'customer': customer
            })
    else:
        redirect('accounts2:signin')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Update successful!", extra_tags='change_password')

            update_session_auth_hash(request, form.user)
            return redirect("accounts2:edit_profile")
        else:
            messages.error(request, "Invalid, try again", extra_tags='change_password')
            return redirect("accounts2:edit_profile")
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, "accounts2/edit_profile.html", {'form': form})

