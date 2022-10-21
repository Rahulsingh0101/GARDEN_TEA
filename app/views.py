from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib import messages
from app.models import Garden

# Create your views here.
# def message(request):
#     return HttpResponse ('hello world')

def about(request):
    return render (request,'id/about.html')    

def contact(request):
    return render (request,'id/contact.html')

def home(request):
    return render (request,'id/home.html')    


def form(request):
    if request.method == 'POST':
        name = request.POST['first_name']
        Email_name = request.POST['Email']
        subject_name= request.POST['subject']
        message = request.POST['message']

        if Garden.objects.filter(Email_name=Email_name).exists():
            messages.error(request,"email already exists")
            return redirect('/')  

       
        else:
            Garden.objects.create(name=name,
                                    Email_name=Email_name,subject_name=subject_name,message=message)
            return redirect('about/')




        