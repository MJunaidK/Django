from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from .models import Product, Order
from django.conf import settings
import stripe, json 
from django.views.decorators.csrf import csrf_exempt
from .forms import ProductForm
# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'myapp/index.html', {'products': products})

def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY

    return render(request, 'myapp/detail.html', {'product': product, 'stripe_publishable_key': stripe_publishable_key})

@csrf_exempt
def create_checkout_session(request, product_id):
    request_data = json.loads(request.body)
    product = Product.objects.get(id=product_id)
    stripe.api_key = settings.STRIPE_SECRET_KEY

    checkout_session = stripe.checkout.Session.create(
       customer_email=request_data['email'],
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': product.name,
                },
                'unit_amount': int(product.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/success/'),
        cancel_url=request.build_absolute_uri('/cancel/'),
    )
    order = Order()
    order.product = product
    order.email = request_data['email']
    order.amount = product.price
    order.stripe_payment_intent = checkout_session.payment_intent
    order.has_paid = False
    order.save()
    return JsonResponse({'id': checkout_session.id})


def payment_success_view(request):
    session_id = request.GET.get('session_id')
    if session_id:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        session = stripe.checkout.Session.retrieve(session_id)
        payment_intent = session.payment_intent

        try:
            order = Order.objects.get(stripe_payment_intent=payment_intent)
            order.has_paid = True
            order.save()
        except Order.DoesNotExist:
            pass
    return render(request, 'myapp/success.html', {'order': order})


def payment_cancel_view(request):
    return render(request, 'myapp/cancel.html')


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'myapp/create_product.html', {'form': form})


def edit_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponseNotFound("Product not found")

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('detail', product_id=product.id)
    else:
        form = ProductForm(instance=product)

    return render(request, 'myapp/edit_product.html', {'form': form, 'product': product}) 

def product_delete(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        return redirect('index')
    except Product.DoesNotExist:
        return HttpResponseNotFound("Product not found")
    


def product_list(request):
     products = Product.objects.all()
     return render(request, 'myapp/product_list.html', {'products': products})   
     