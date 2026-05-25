from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm
from django.contrib.auth.models import User
from datetime import datetime


def dashboard(request):

    expenses = Expense.objects.all()

    total_expense = 0

    food_total = 0
    travel_total = 0
    shopping_total = 0
    bills_total = 0

    for expense in expenses:

        total_expense += expense.amount

        if expense.category == 'Food':
            food_total += expense.amount

        elif expense.category == 'Travel':
            travel_total += expense.amount

        elif expense.category == 'Shopping':
            shopping_total += expense.amount

        elif expense.category == 'Bills':
            bills_total += expense.amount

    current_month = datetime.now().month

    monthly_total = 0

    for expense in expenses:

        if expense.date.month == current_month:
            monthly_total += expense.amount

    highest_category = ""

    highest_amount = max(
        food_total,
        travel_total,
        shopping_total,
        bills_total
    )

    if highest_amount == food_total:
        highest_category = "Food"

    elif highest_amount == travel_total:
        highest_category = "Travel"

    elif highest_amount == shopping_total:
        highest_category = "Shopping"

    elif highest_amount == bills_total:
        highest_category = "Bills"


    insight_message = f"You spent the most on {highest_category}."

    context = {
        'expenses': expenses,
        'total_expense': total_expense,

        'food_total': food_total,
        'travel_total': travel_total,
        'shopping_total': shopping_total,
        'bills_total': bills_total,
        'monthly_total': monthly_total,

        'insight_message': insight_message,
    }

    return render(request, 'dashboard.html', context)


def add_expense(request):

    if request.method == 'POST':

        form = ExpenseForm(request.POST)

        if form.is_valid():

            expense = form.save(commit=False)

            expense.user = User.objects.first()

            expense.save()

            return redirect('dashboard')

    else:

        form = ExpenseForm()

    return render(request, 'add_expense.html', {'form': form})


def delete_expense(request, id):

    expense = Expense.objects.get(id=id)

    expense.delete()

    return redirect('dashboard')


def edit_expense(request, id):

    expense = Expense.objects.get(id=id)

    if request.method == 'POST':

        form = ExpenseForm(request.POST, instance=expense)

        if form.is_valid():

            form.save()

            return redirect('dashboard')

    else:

        form = ExpenseForm(instance=expense)

    return render(request, 'add_expense.html', {'form': form})