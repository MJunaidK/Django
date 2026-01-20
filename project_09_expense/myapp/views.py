from django.shortcuts import render
from django.db.models import Sum
from .models import Expense
from.forms import ExpenseForm
from django.shortcuts import get_object_or_404, redirect
import datetime

# Create your views here.

def index(request):
    if request.method == 'POST':
        expense_form = ExpenseForm(request.POST)
        if expense_form.is_valid():
            expense_form.save()
    expenses = Expense.objects.all()   
    total_expense = sum(expense.amount for expense in expenses)
    last_year= datetime.date.today() - datetime.timedelta(days=365)
    data = Expense.objects.filter(date__gte=last_year)
    yearly_sum = data.aggregate(total=Sum('amount'))['total'] or 0

    last_month= datetime.date.today() - datetime.timedelta(days=30)
    data = Expense.objects.filter(date__gte=last_month)
    monthly_sum = data.aggregate(total=Sum('amount'))['total'] or 0

    last_week= datetime.date.today() - datetime.timedelta(days=7)
    data = Expense.objects.filter(date__gte=last_week)
    weekly_sum = data.aggregate(total=Sum('amount'))['total'] or 0

    daily_sums = Expense.objects.filter().values('date').order_by('date').annotate(total=Sum('amount'))

    categorical_sums = Expense.objects.filter().values('category').order_by('category').annotate(total=Sum('amount'))

    print(total_expense)
    print(yearly_sum)     
    print(daily_sums)
    expense_form = ExpenseForm()
    return render(request, 'myapp/index.html', {'expense_form': expense_form, 'expenses': expenses, 'total_expense': total_expense, 'yearly_sum': yearly_sum, 'monthly_sum': monthly_sum, 'weekly_sum': weekly_sum, 'daily_sums': daily_sums, 'categorical_sums': categorical_sums})

def edit_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    if request.method == 'POST':
        expense_form = ExpenseForm(request.POST, instance=expense)
        if expense_form.is_valid():
            expense_form.save()
    expense_form = ExpenseForm(instance=expense)
    return render(request, 'myapp/edit.html', {'expense_form': expense_form})


def delete_expense(request, expense_id):
    if request.method == 'POST' and 'delete' in request.POST:
        expense = get_object_or_404(Expense, id=expense_id)
        expense.delete()
    return redirect('index')