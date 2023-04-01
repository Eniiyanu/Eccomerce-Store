from django import forms
from django_countries.fields import CountryField




class DeliveryAddressForm(forms.Form):
    first_name =  forms.CharField()
    last_name =  forms.CharField()
    email = forms.CharField()
    address_line_1 = forms.CharField()
    address_line_2 = forms.CharField(required=False)
    state = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    phone = forms.CharField()


    #country = CountryField(blank_label='(Select country)',).formfield(widget=CountrySelectWidget(attrs={ 'class':custom-select d-block w-100}) )
