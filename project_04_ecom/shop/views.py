from django.shortcuts import render
from .models import Order, Product
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    item_name = request.GET.get('item_name')

    # Step 1: Start with a QuerySet
    product_objects = Product.objects.all()

    # Step 2: Apply filters BEFORE pagination
    if item_name:
        product_objects = product_objects.filter(title__icontains=item_name)

    # Step 3: Paginate the filtered QuerySet
    paginator = Paginator(product_objects, 4)
    page_number = request.GET.get('page')
    product_objects = paginator.get_page(page_number)

    return render(request, 'shop/index.html', {'products': product_objects})

def detail(request, id ):
    product_object = Product.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product': product_object})

def checkout(request):
    if request.method == 'POST':
        items=request.POST.get('items', '')     
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')   
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zipcode = request.POST.get('zipcode', '')
        total_amount = request.POST.get('total_amount', '0.00') 
        print(items, name, email, address, city, state, zipcode)
    
        order = Order(
            items = items,
            name = name,
            email = email,      
            address = address,
            city = city,
            state = state,
            zipcode = zipcode,
            total_amount = total_amount

        )
        order.save()
    return render(request, 'shop/checkout.html')