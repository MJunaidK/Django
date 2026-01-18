from django.shortcuts import get_object_or_404, redirect, render
from .models import Consume, Food
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
 
    if request.method =="POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user,food_consumed=consume)
        consume.save()
        foods = Food.objects.all()
 
 
    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)
 
    return render(request,'myapp/index.html',{'foods':foods,'consumed_food':consumed_food})
 
def delete_consume(request,id):
    consumed_food = Consume.objects.get(id=id)
    if request.method =='POST':
        consumed_food.delete()
        return redirect('/')
    return render(request,'myapp/delete.html')

def index(request):

    if request.method == 'POST':
        food_consumed_id = request.POST.get('food_consumed')

        if food_consumed_id:
            food = get_object_or_404(Food, id=food_consumed_id)
            user = request.user
            Consume.objects.create(user=user, food_consumed=food)

    # Load consumed foods for the user (works for both GET and POST)
    consumed_food = Consume.objects.filter(user=request.user)
    print("Consumed Food:", consumed_food)

    # Load foods the user has NOT consumed yet
    foods = Food.objects.exclude(
        id__in=consumed_food.values_list('food_consumed__id', flat=True)
    )

    return render(request, 'myapp/index.html', {
        'foods': foods,
        'consumed_food': consumed_food
    })

def delete_consumed_food(request, consume_id):
    consume_entry = get_object_or_404(Consume, id=consume_id, user=request.user)
    if request.method == 'POST':
        consume_entry.delete()
        return redirect('/') 
    return render(request, 'myapp/delete.html')