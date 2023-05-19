from django.shortcuts import render

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
def appointment(request):
    if request.method == 'POST':
        # Extract form data from the request
        first_name = request.POST.get('f_name')
        last_name = request.POST.get('l_name')
        birthdate = request.POST.get('birthdate')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dentist = request.POST.get('dentist')
        timeslots = request.POST.get('timeslots')

        # Save the form data to the database or perform other actions
        # Example using Django's ORM:
        # from .models import Booking
        # booking = Booking(first_name=first_name, last_name=last_name, birthdate=birthdate, email=email, phone=phone, dentist=dentist, timeslot=timeslot)
        # booking.save()

        # Redirect to a success page or render a success message
        return render(request, 'TheKiddoDontist/OnlineBooking.html',{'dentist':dentist})

    return render(request, 'TheKiddoDontist/appointment.html')


