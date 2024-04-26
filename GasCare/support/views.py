from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate,login,logout
from support.models import User, ServiceRequest
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from twilio.rest import Client

# Create your views here.
def signup(request):
    context = {}
    if request.method == "POST":
        uname = request.POST.get('uname')
        uemail = request.POST.get('uemail')
        upassword = request.POST.get('upassword')
        cpassword = request.POST.get('cpassword')
        if uname == "" or uemail == "" or upassword == "" or cpassword == "":
            context['error'] = "All fields are required"
        elif upassword != cpassword:
            context['error'] = "Passwords did not match"
        else:
            try:
                u = User.objects.create_user(username=uname, email=uemail, password=upassword)
                u.save()
                return redirect('signin')
            except Exception:
                context["error"] = "User already exists"
    return render(request, "sign-up.html", context)
            
def signin(request):
    context = {}
    if request.method == "POST":
        nm = request.POST["uname"]
        pw = request.POST["upassword"]  
        if nm == "" or pw == "":
            context['errmsg'] = "Fields cannot be Empty"
            return render(request, "sign-in.html", context)
        else:
            user = authenticate(username=nm, password=pw)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                context["errmsg"] = "Invalid Username and password"
                return render(request, "sign-in.html", context)
    else:
        return render(request, "sign-in.html")
    
def user_logout(request):
    print(request.user)
    logout(request)
    return redirect('/signin/')

def user_name(request):
    user = request.user
    return render (request, "index.html", user)
    
def home(request):
    return render(request, "index.html")

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

@login_required
def service(request):
    if request.user.is_authenticated and  request.method == "POST":
        user_id = request.user
        name = request.POST["uname"]
        email = request.POST["uemail"]
        phone = request.POST["uphone"]
        service = request.POST["uservice"]
        msg = request.POST["umessage"]
        m = ServiceRequest.objects.create( user_id=user_id , name = name, email = email, phone_number= phone, message = msg, service = service)
        status = m.status
        plain_message = f"name: {name}\n\n email: {email}\n\n phone: {phone}\n\n Service requested: {service}\n\n Status: {status}"
        send_mail(
            'GasCare',
            plain_message,
            'thakurkaustubh37@gmail.com',
            [m.email],
            fail_silently=False,
        )
        message_body = f"name: {name}\n\n email: {email}\n\n phone: {phone}\n\n Service requested: {service}\n\n Status: {status}"
        message = client.messages.create(
        from_='+12567279802',
        body=message_body,
        to='+919156748282')
        m.save()
        return redirect('home')
    
@receiver(post_save, sender=ServiceRequest)
def send_status_change_notification(sender, instance, **kwargs):
    if instance.status == 'Resolved':
        subject = f"Service status is Resolved"
        message = f"Dear {instance.name}, your request for the service of {instance.service} is resolved, Thank You for choosing us!!"
        from_email = 'thakurkaustubh37@gmail.com'
        recipient_list = [instance.email]
        send_mail(subject, message, from_email, recipient_list)
        message_body = f"Dear {instance.name}, your request for the service of {instance.service} is resolved, Thank You for choosing us!!"
        message = client.messages.create(
        from_='+12567279802',
        body=message_body,
        to='+919156748282')

def service_view(request):
    service_requests = ServiceRequest.objects.filter(user_id=request.user.id)
    return render(request, 'status.html', {'service_requests': service_requests})

def deleterequest(request, dreq):
    m = ServiceRequest.objects.filter(status='In Progress', id=dreq)
    if m.exists():
        m.delete()
        return redirect('status')
        
