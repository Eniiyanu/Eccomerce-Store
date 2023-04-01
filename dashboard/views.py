from django.shortcuts import render, reverse,redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView, TemplateView
from django.contrib.admin.views.decorators import staff_member_required
from product.models import *
from django.views import generic
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
import sweetify

# Create your views here.
class IndexView(generic.View):
	model = Product
	paginate_by = 5
	def get(self, *args, **kwargs):
		
		wishlist = Wishlist.objects.filter(customer= self.request.user)

		context = {
				'wishlist':wishlist
			}
		return render (self.request, "dashboard/dashboard-index.html" , context)
def addWishlist(request):
	if request.method == 'POST':
		product_id = request.POST.get('product_id')

		try:
			Wishlist.objects.create(user = request.user, product= product_id) 

		except:
			wish_item = Wishlist.objects.get(user = request.user, product= product_id)  
			if wish_item:
    			
    			#wish_item.quantity += 1
				wish_item.save()	
		
		
		finally:
			return redirect( str('dashboard-index'))
		

def deletewishlist(request, id):
    customer=request.user.customer
    Wishlist.objects.filter(customer_id=customer.id, product=Product.objects.get(id=id)).delete()
    #messages.success(request, 'Product Remove From Wishlist...')
    return HttpResponseRedirect('/dashboard')


class OrderDetailView(UpdateView):
	model = Order
	fields = ['status']
	template_name = "dashboard/dashboard-index.html"

	def get_success_url(self):
		return reverse('order-details', kwargs={'pk': self.object.id})

class ProductCreateView(CreateView):
	template_name = "forms.html"
	model = Product
	fields = ['image', 'name', 'description', 'price', 'available_units', 'category', 'tags']

	def get_success_url(self):
		return reverse('dashboard-index')

class ProductListView(ListView):
	template_name = "dashboard/productlist.html"

	def get_queryset(self):
		return Product.objects.all()

class ProductEditView(UpdateView):
	template_name = "forms.html"
	model = Product
	fields = ['image', 'name', 'description', 'price', 'available_units', 'category', 'tags']

	def get_success_url(self):
		return reverse('product-edit', kwargs={'pk': self.object.id})

class PendingOrdersView(TemplateView):
	template_name = "dashboard/pendingorders.html"


