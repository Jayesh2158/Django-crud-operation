import datetime
from django.shortcuts import redirect, render
from .models import *
from .forms import AddUser, ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.core.mail import send_mail
import uuid
# from django.contrib.auth import authenticate, login


def home(request):
    # import pdb
    # pdb.set_trace()
    if request.method == 'POST':
        pass
        # return redirect(request, 'add_item.html')
        # form = ListForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     all_items = list.objects.all()
        #     messages.success(request, ('Item has been addes to list!'))
        #     return render(request, 'home.html', {'all_item': all_items})
    else:
        all_items = list.objects.all()
        return render(request, 'home.html', {'all_item': all_items})


def about(request):
    # context = {'first_name': 'John', 'last_name': 'Elder'}
    return render(request, 'about.html', {})


def delete(request, list_id):
    item = list.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item has been deleted'))
    return redirect('home')


def cross_off(request, list_id):
    item = list.objects.get(pk=list_id)
    item.complete = True
    item.save()
    return redirect('home')


def uncross(request, list_id):
    item = list.objects.get(pk=list_id)
    item.complete = False
    item.save()
    return redirect('home')


def edit(request, list_id):
    # import pdb
    # pdb.set_trace()
    # item = list.objects.get(pk=list_id)
    if request.method == 'POST':
        print('edit post')
        item = list.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)
        # import pdb;pdb.set_trace()
        if form.is_valid():
            form.save()
            messages.success(request, ('Item Has Been Edited!'))
            return redirect('home')
        else:
            error = form.errors
            # messages.success(request, (error))
            return render(request, 'edit.html', {'errors': error, 'item': item})

    else:
        item = list.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})


def addItem(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            all_items = list.objects.all()
            messages.success(request, ('Item has been added to list!'))
            return render(request, 'home.html', {'all_item': all_items})
        else:
            error = form.errors
            return render(request, 'add_item.html', {'errors': error})
    else:
        return render(request, 'add_item.html')


# def adduser(request):
#     if request.method == 'POST':
#         import pdb
#         pdb.set_trace()
#         form = AddUser(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return render(request, 'login_user.html')
#         else:
#             error = form.errors
#             return render(request, 'add_user.html', {'errors': error})
#     else:
#         return render(request, 'add_user.html')


def Login(request):
    if request.method == 'POST':
        import pdb
        pdb.set_trace()
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = authenticate(username=username, password=password)
        except:
            messages.success(
                request, ('User does not exist or password may wrong !'))

        if user is not None:
            #login(request, user)
            return redirect('home')
        return redirect('login')
    else:
        return render(request, 'login_user.html')


def sendMail(email, token, name):
    subject = 'Here is your password reset link.'
    message = f'Hello! {name}, your password reset link is http://127.0.0.1:8000/reset/{token} '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    print("Mail sent successfully")


def forgot(request):
    if request.method == 'POST':
        user_mail = request.POST['email']
        try:
            valid_user = User.objects.get(email=user_mail)
        except:
            messages.success(request, ('Invalid mail!'))
            return redirect('forgot')
        token = str(uuid.uuid4())
        valid_user.token = token
        valid_user.token_check = True
        valid_user.token_time = timezone.now()
        valid_user.save()
        sendMail(user_mail, token, valid_user.name)
        messages.success(request, ('Email Sent'))
        return redirect('forgot')
    else:
        return render(request, 'forgot.html')


def reset(request, tokenId):
    try:
        user = User.objects.filter(token=tokenId).first()
    except:
        render(request, '404.html')
    if request.method == "POST":
        password = request.POST['password']
        confirmPass = request.POST['confirmPassword']

        if password != confirmPass:
            return render(request, 'resetPass.html', {"confirm": True})
        user.password = password
        user.token_check = False
        user.save()
        return render(request, 'success.html')
    else:

        if user.token_check == False:
            return render(request, '404.html')
        sec = datetime.timedelta(seconds=600)
        if timezone.now()-user.token_time >= sec:
            return render(request, '404.html')
        return render(request, 'resetPass.html')


def error404(request):
    return render(request, '404.html')


def Sucess(request):
    return render(request, 'success.html')


def profile(request):
    return render(request, 'profile.html')


def register_request(request):
    if request.method == "POST":
        # import pdb
        # pdb.set_trace()
        form = AddUser(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("login")

        errors = form.errors
        messages.success(request, ("Somthing went wrong."))
        return render(request, "register.html", {"register_form": form})
    form = AddUser()
    return render(request, "register.html", {"register_form": form})

def profileView(request):
    return render(request,"profile_view.html")