from django.urls import path
from .import views
urlpatterns = [
    path('', views.home,name='TheKiddoDontist-home'),
    path('aboutus', views.aboutus,name='TheKiddoDontist-aboutus'),
    path('PediatricDentistry', views.PediatricDentistry,name='TheKiddoDontist-PediatricDentistry'),
    path('GeneralAnesthesia', views.GeneralAnesthesia,name='TheKiddoDontist-GeneralAnesthesia'),
    path('contactus', views.contactus,name='TheKiddoDontist-contactus'),
    path('OnlineBooking', views.OnlineBooking,name='TheKiddoDontist-OnlineBooking'),
    path('Reviews', views.Reviews,name='TheKiddoDontist-Reviews'),
    path('login', views.login,name='TheKiddoDontist-login'),
]
