from django.shortcuts import render
from .models import Appointment
from django.shortcuts import redirect

def home(request):
    return render(request,'TheKiddoDontist/homepage.html')
def aboutus(request):
    return render(request,'TheKiddoDontist/7anafy.html')
def PediatricDentistry(request):
    return render(request,'TheKiddoDontist/PediatricDentistry.html')
def GeneralAnesthesia(request):
    return render(request,'TheKiddoDontist/GeneralAnesthesia.html')
def contactus(request):
    return render(request,'TheKiddoDontist/contactus.html')
def OnlineBooking(request):
    return render(request,'TheKiddoDontist/OnlineBooking.html')
def Reviews(request):
    return render(request,'TheKiddoDontist/Reviews.html')
def login(request):
    return render(request,'TheKiddoDontist/login.html')


def submit_appointment(request):
    if request.method == 'POST':
        # Get form data
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        birthdate = request.POST['birthdate']
        email = request.POST['email']
        phone = request.POST['phone']
        dentist = request.POST['dentist']
        timeslot = request.POST['timeslots']

        # Create Appointment instance
        appointment = Appointment(
            first_name=first_name,
            last_name=last_name,
            birthdate=birthdate,
            email=email,
            phone=phone,
            dentist=dentist,
            timeslot=timeslot
        )

        # Save the appointment
        appointment.save()

        # Redirect to the appointments page
        return redirect('OnlineBooking')

    # Handle GET request if needed


def appointment(request):
    appointments = Appointment.objects.all()
    return render(request, 'TheKiddoDontist/appointment.html', {'appointments': appointments})

