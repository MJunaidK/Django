from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import ItemForm
from .models import Item

# Create your views here.
def index(request):
    item_list=Item.objects.all()
    return render(request, 'myapp/index.html', {'item_list': item_list})

def detail(request, item_id):
    item =  Item.objects.get(id=item_id)
    return render(request, 'myapp/detail.html', {'item': item})

# def item(request):
#     return HttpResponse("<h1>This is an item view</h1>")

def create_item(request):
    form = ItemForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('myapp:index')
    return render(request, 'myapp/item-form.html', {'form': form})


def update_item(request, item_id): 
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('myapp:index')
    return render(request, 'myapp/item-form.html', {'form': form}) 

def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('myapp:index')
    return render(request, 'myapp/item-delete.html', {'item': item})