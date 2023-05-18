from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
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
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

