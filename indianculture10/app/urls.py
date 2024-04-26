from django.urls import *
from .views import *

urlpatterns=[
    path('',home,name="home"),
    path('signup',signup,name="signup"),
    path('contactus',contactus,name="contactus"),
    path('aboutus',aboutus,name="aboutus"),
    path('offerings',offerings,name="offerings"),

]