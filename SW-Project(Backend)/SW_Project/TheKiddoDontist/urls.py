from django.urls import path
from .import views
urlpatterns = [
    path('', views.home,name='TheKiddoDontist-home'),
    path('aboutus', views.aboutus,name='TheKiddoDontist-aboutus'),
    path('PediatricDentistry', views.PediatricDentistry,name='TheKiddoDontist-PediatricDentistry'),
]
