from django.shortcuts import render

def home(request):
    return render(request,'TheKiddoDontist/homepage.html')
def aboutus(request):
    return render(request,'TheKiddoDontist/7anafy.html')
def PediatricDentistry(request):
    return render(request,'TheKiddoDontist/PediatricDentistry.html')