from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Access/$',Access,name="Access"),
	url(r'^Login/$',Login,name="Login"),
	url(r'^Register/$',Register,name="Register"),
	url(r'^Profile/$',Profile,name="Profile"),
	url(r'^LogOut/$',LogOut,name="LogOut"),
]