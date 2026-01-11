from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ItemForm
from .models import Item
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy    
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
import logging
from django.shortcuts import get_object_or_404
from django.utils import timezone
# Create your views here.

logger = logging.getLogger(__name__)
# @login_required
# def index(request):
    # item_list=Item.objects.all()
    # return render(request, 'myapp/index.html', {'item_list': item_list})

#@cache_page(60)  # Cache the view for 60 seconds
#@vary_on_headers("User-Agent")    
def index(request):
    logger.info("Index view accessed")
    logger.info(f"User [{timezone.now().isoformat()}] {request.user} is accessing the index page from IP: {request.META.get('REMOTE_ADDR')}")
    item_list = Item.objects.all()
    logger.debug(f"Fetched {item_list.count()} items from the database")
    paginator = Paginator(item_list, 5)  # Show 5 items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'myapp/index.html', {'page_obj': page_obj})


class IndexClassView(ListView):
    model = Item
    template_name = 'myapp/index.html'
    context_object_name = 'item_list'


def detail(request, item_id):
    logger.info(f"Detail view accessed for item_id: {item_id}")
    try:
        # item = get_object_or_404(Item, id=item_id)
        item = Item.objects.get(id=item_id)
        logger.debug(f"Fetched item: {item}") 
    except Item.DoesNotExist:
        logger.error(f"Item with id {item_id} does not exist")
        return HttpResponse("Item not found", status=404)
    except Exception as e:
        logger.error(f"Error fetching item with id {item_id}: {e}")
    return render(request, 'myapp/detail.html', {'item': item})

# class DetailClassView(DetailView):
    # model = Item
    # template_name = 'myapp/detail.html'
    # context_object_name = 'item'

# def item(request):
#     return HttpResponse("<h1>This is an item view</h1>")

# def create_item(request):
    # form = ItemForm(request.POST or None)
    # if request.method == 'POST':
        # if form.is_valid():
            # form.save()
            # return redirect('myapp:index')
    # return render(request, 'myapp/item-form.html', {'form': form})

class ItemCreateView(CreateView):
    model = Item 
    form_class = ItemForm
    template_name = 'myapp/item-form.html'
    # success_url = reverse_lazy('myapp:index')

# def update_item(request, item_id): 
    # item = Item.objects.get(id=item_id)
    # form = ItemForm(request.POST or None, instance=item)
    # if request.method == 'POST':
        # if form.is_valid():
            # form.save()
            # return redirect('myapp:index')
    # return render(request, 'myapp/item-form.html', {'form': form}) 

class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name_suffix = '_update_form'

    def get_queryset(self):
        return super().get_queryset().filter(user_name=self.request.user)
    

# def delete_item(request, item_id):
    # item = Item.objects.get(id=item_id)
    # if request.method == 'POST':
        # item.delete()
        # return redirect('myapp:index')
    # return render(request, 'myapp/item-delete.html', {'item': item})

class DeleteItemView(DeleteView):
    model = Item
    success_url = reverse_lazy('myapp:index')