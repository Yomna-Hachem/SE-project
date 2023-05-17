from django.shortcuts import render

def home(request):
    return render(request,'TheKiddoDontist/homepage.html')
def aboutus(request):
    return render(request,'TheKiddoDontist/7anafy.html')
<<<<<<< HEAD
def onlineBooking(request):
     return render(request,'TheKiddoDontist/OnlineBooking.html')
=======
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

>>>>>>> aad6f5efa8b50ca02b1f33d85f02eec9f8701658
