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

