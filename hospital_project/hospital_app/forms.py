from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type= 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'

        widgets={
            'booking_date':DateInput(),
        }
        labels={
            'p_name':'Patient Name',
            'p_phone':'Patient Contact Number',
            'p_email':'Email-id',
            'dep_name':'Doctors Department',
            'doc_name': "Doctor's Name",
            'booking_date':"Booking Date",
        }