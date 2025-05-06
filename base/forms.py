from django import forms
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class InsuranceForm(forms.Form):
    first_name = forms.CharField(max_length=100, label='First Name')
    last_name = forms.CharField(max_length=100, label='Last Name')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(max_length=9, label='Phone Number')
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(choices=[
        ('female', 'Female'),
        ('male', 'Male'),
    ], label="Gender")
    vehicle_type = forms.ChoiceField(choices=[
        ('car', 'Car'),
        ('motorcycle', 'Motorcycle'),
        ('truck', 'Truck'),
    ], label='Vehicle Type')
    insurance_type = forms.ChoiceField(choices=[
        ('OC', 'OC'),
        ('OC + NNW', 'OC + NWW'),
        ('OC + AC + NNW', 'OC + AC + NWW'),
    ], label='Insurance Type')
    vehicle_price = forms.DecimalField(max_digits=10, decimal_places=2, label='Vehicle Price')
    mileage_per_year = forms.IntegerField(label='Mileage per Year')

    start_date = forms.DateField(widget=forms.SelectDateWidget(), label='Start Date',
                                 initial=(datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d"))
    end_date = forms.DateField(widget=forms.SelectDateWidget(), label='End Date',
                               initial=(datetime.today() + relativedelta(days=1, years=1)).strftime("%Y-%m-%d"))
    previous_insurance = forms.BooleanField(required=False, initial=True, label='Previous Insurance')
    previous_accidents = forms.IntegerField(required=True, initial=0, label='Previous Accidents')
    country = forms.CharField(max_length=100, label='Country')
    city = forms.CharField(max_length=100, label='City')
