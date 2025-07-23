from django.contrib import admin
from django.urls import path,include
from website.views import *
urlpatterns = [
   
  path('',index,name='index'),  # Include the URLs from the website app
  path('about/',about,name='about'),  # Include the URLs from the website app
  path('contact/',contact,name='contact'),  # Include the URLs from the website app
  path('careers/',careers,name='careers'),  # Include the URLs from the website app
  path('services/',services,name='services'),  # Include the URLs from the website app
  path('industries/',industries,name='industries'),  # Include the URLs from the website app
  path('login_view/',login_view,name='login_view'),  # Include the URLs from the website app
  path('cybersecurity/',cyber_security,name='cybersecurity'),  # Include the URLs from the website app
  path('software_development/',software_development,name='software_development'),  # Include the URLs from the website app
  path('website_development/',website_development,name='website_development'),  # Include the URLs from the website app
  path('application_development/',application_development,name='application_development'),  # Include the URLs from the website app
  path('data_science/',data_science,name='data_science'),  # Include the URLs from the website app
  path('artificial_intelligence/',artificial_intelligence,name='artificial_intelligence'),  # Include the URLs from the website app
]