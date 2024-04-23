from django.shortcuts import render, HttpResponse

# Create your views here.
def signup(request):
    return render (request,"sign-up.html")

def signin(request):
    return render(request, "sign-in.html")