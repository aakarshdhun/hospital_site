from django.shortcuts import render
from .models import Department,Doctors
from .forms import BookingForm
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def departments(request):
    dep=Department.objects.all()
    return render(request, 'departments.html',{'dep':dep})

def doctors(request):
    doc={"doc":Doctors.objects.all()}
    return render(request, 'doctors.html',doc)

def appointment(request):
    if request.method =='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'thankyou.html')
    form=BookingForm()
    dict={"form":form}
    return render(request, 'appointment.html',dict)

def contact(request):
    return render(request,'contact.html')



