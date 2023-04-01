from django.shortcuts import render, reverse,redirect
from product.models import *
from customer.models import Customer, Address
from django.http import HttpResponse, JsonResponse
from django.views.generic import UpdateView,FormView,CreateView, View
import requests
import json
import datetime
import os
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
import environ
from django.urls import reverse_lazy
from  .forms import DeliveryAddressForm
import sweetify
from django.contrib import messages
from django.contrib.auth.decorators import login_required


env = environ.Env()
# reading .env file
environ.Env.read_env()
PAYSTACK_SECRET_KEY= env('PAYSTACK_SECRET_KEY')
PAYSTACK_PUBLIC_KEY= env('PAYSTACK_PUBLIC_KEY')

class DeliveryInfo(CreateView):
	def get(self, *args, **kwargs):
		form = DeliveryAddressForm
		context ={
			'form':form
		}
		return render(self.request, "forms.html",context)

	
	def get_object(self):
		user = self.request.user
		deviceId = self.request.COOKIES["deviceId"] 
		try:
			customer= Customer.objects.get(user = user)
		except:
			customer, created = Customer.objects.get_or_create(device_id = deviceId)
		
		return customer
	def post(self,*args, **kwargs):
		user = self.request.user
		form = DeliveryAddressForm(self.request.POST or None)
		
		try:
			address = Address.objects.get(first_name=first_name, last_name=last_name, email=email, address_line_1=address_line_1,
			state=state, address_line_2=address_line_2,city=city,country=country,phone=phone)
		except:
			if form.is_valid():
				first_name = form.cleaned_data.get('first_name')
				last_name =  form.cleaned_data.get('last_name')
				email =  form.cleaned_data.get('email')
				address_line_1 = form.cleaned_data.get('address_line_1')
				address_line_2 =form.cleaned_data.get('address_line_2')
				state =form.cleaned_data.get('state')
				city = form.cleaned_data.get('city')
				country =form.cleaned_data.get('country')
				phone = form.cleaned_data.get('phone')
				billing_address = Address(
					#user= self.request.user,
					first_name =first_name,
					last_name = last_name,
					email = email,
					state = state,
					city = city,
					country = country,
					phone = phone,
					address_line_1 = address_line_1,
					address_line_2 = address_line_2,
				)
				billing_address.save()
				
				messages.success(self.request,"Billing address saved")
			return redirect('checkout')
	


def CheckoutView(request):
	template = "checkout.html"

	address = Address.objects.all().last()
	try:
		customer = Customer.objects.get(user = request.user)
	except:
		deviceId = request.COOKIES["deviceId"]
		customer, created = Customer.objects.get_or_create(device_id = deviceId)
	order, created = Order.objects.get_or_create(customer = customer, completed = False)
	string = str(datetime.datetime.now().timestamp())
	order.state = address
	order.transaction_id = string
	order.save()
	
	

	#user = User.objects.all().last()
	
	cartitems = order.cartitem_set.all()
	return render(request, template, {  "order":order,"address":address,
	"cartitems":cartitems, })

def InitializePaymentView(request):
	data = json.loads(request.body)
	headers = {'Authorization': f"Bearer ********",'Content-Type': 'application/json'}
	res = requests.post('https://api.paystack.co/transaction/initialize', headers=headers, json = data, )

	#print (res.text)
	response = res.json()
	print (response)
	return JsonResponse(response)

def VerifyPaymentView(request, *args, **kwargs):
	reference = request.GET['trxref']
	order = Order.objects.get(transaction_id = reference)
	print (reference)
	url = 'https://api.paystack.co/transaction/verify/'
	verify_url = url + reference
	headers = {'Authorization': f"Bearer *************",'Content-Type': 'application/json'}
	res = requests.get(verify_url, headers=headers, )
	response = res.json()
	if res.ok == True:
		content = json.loads(res.content)
		message = content["message"]
		if message == "Verification successful":
			order.completed = True
			order.save()
			cartitems = order.cartitem_set.all()
			purchased = ','.join([str(elem) for elem in cartitems])
			user = request.user
			location = Address.objects.all().last()
			
			first_name = Address.objects.get('first_name')
			last_name = Address.objects.get('last_name')
			email = Address.objects.get('email')
			
			DEFAULT_FROM_EMAIL = 'Daamz Hair Sales<info@daamzhair.com.ng>'
			subject = ' Purchase Confirmation'
			message = f'This is to notify you {first_name} {last_name} made a purchase of {purchased}. Our Sales Representative would attend to you shortly. On this email; {email} Our courier service would contact you shortly and  products would be delivered to {location}'
			from_email =settings.EMAIL_HOST_USER
			recipient_list = [email,'info@daamzhair.com.ng'] 
			send_mail(subject,message,DEFAULT_FROM_EMAIL,recipient_list, fail_silently=False)
		



			
		return redirect('/')
	else:
		message = "Operation failed"

	return HttpResponse(message)