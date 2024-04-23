from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate,login,logout
from support.models import User

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
                return HttpResponse("Done!!")
            except Exception:
                context["error"] = "User already exists"
    return render(request, "sign-up.html", context)
            
def signin(request):
    context = {}
    if request.method == "POST":
        nm = request.POST["uname"] # Using get() method to avoid errors
        pw = request.POST["upassword"]  # Using get() method to avoid errors
        if nm == "" or pw == "":
            context['errmsg'] = "Fields cannot be Empty"
            return render(request, "sign-in.html", context)
        else:
            user = authenticate(username=nm, password=pw)
            if user is not None:
                login(request, user)
                return HttpResponse("Logged in successfully!")
            else:
                context["errmsg"] = "Invalid Username and password"
                return render(request, "sign-in.html", context)
    else:
        return render(request, "sign-in.html")