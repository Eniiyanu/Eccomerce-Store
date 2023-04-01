from django.urls import path, re_path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
	path('', views.CheckoutView, name = "checkout" ),
    
	path('delivery-info', (views.DeliveryInfo.as_view()), name = "delivery_info"),
    path('initialize/payment/', views.InitializePaymentView, name = "payment_init"),
    path('verify/', views.VerifyPaymentView, name = "verify_payment"),
]