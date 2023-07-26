from django.shortcuts import render

# Create your views here.
from .models import *

from django.http import HttpResponse

from instamojo_wrapper import Instamojo
from django.conf import settings

api = Instamojo(api_key=settings.API_KEY , auth_token=settings.AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/')

print(">>>>>>>>" , api)

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products' : products})

def order(request, product_id):
    try:
        print(">>>>>>>>" , product_id)
        product_obj = Product.objects.get(uid=product_id)
        print("product_obj >>>>" , product_obj.uid)
        order_obj, _  = Order.objects.get_or_create(
            product_id=product_obj.uid,
            user=request.user,
            is_paid=False
        )

        print("order_obj >>>>" , order_obj)


        response = api.payment_request_create(
            amount=order_obj.product.product_price,  # Corrected the field name
            purpose='Order Process',
            buyer_name='Vj1',
            email='vj1@gmail.com',
            redirect_url='http://127.0.0.1:8000/order-success/'
        )

        print(">>>>>>" , response)

        order_obj.order_id = response['payment_request']['id']
        order_obj.instamojo_response = response

        print("Order ID " , type(order_obj.order_id))
        print("Order ID " , order_obj.order_id)

        order_obj.save()

        return render (request , 'order.html', context = {
            'payment_url' : response['payment_request']['longurl']

        })
        

        # Return a response to avoid the 'The view didn't return an HttpResponse object' error
        return HttpResponse("Order request created successfully. Payment link generated.")

    except Exception as e:
        print(e)
        return HttpResponse("An error occurred while processing your order.")


def order_success(request):
    print("order_success request.GET ====>>>>  " , request.GET)
    payment_request_id = request.GET.get('payment_request_id')
    payment_id = request.GET.get('payment_id')
    print("payment_id======>>>", payment_id)

    print(" payment_request_id ====>>>> " , payment_request_id)

    order_obj = Order.objects.get(order_id = payment_request_id) 
    print("order_obj ==== >>>>  " , order_obj)
    order_obj.is_paid = True
    order_obj.save()
    return HttpResponse('Payment success')
















