from django.shortcuts import render

def home(request):
    return render(request,'TheKiddoDontist/homepage.html')
def aboutus(request):
    return render(request,'TheKiddoDontist/7anafy.html')