from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name=models.CharField(max_length=250)
    dep_description=models.TextField()

    def __str__(self):
        return self.dep_name

class Doctors(models.Model):
    doc_name=models.CharField(max_length=250)
    doc_spec=models.CharField(max_length=250)
    dep_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to='pics')

    def __str__(self):
        return ('{} - {}').format(self.doc_name,self.dep_name)

class Booking(models.Model):
    p_name=models.CharField(max_length=250)
    p_phone=models.IntegerField()
    p_email=models.EmailField()
    dep_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)