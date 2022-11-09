from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('departments/',views.departments,name='departments'),
    path('doctors/',views.doctors,name='doctors'),
    path('appointment/',views.appointment,name='appointment'),
    path('contact/',views.contact,name='contact'),

]