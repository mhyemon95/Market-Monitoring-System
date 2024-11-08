# dashboard/views.py
from django.shortcuts import render
from django.contrib.auth.models import User  # Example: to get the user count
from .models import Order  # Assuming you have an Order model for revenue data
from datetime import date

def dashboard_home(request):
    # Example data: replace these with real data from your models
    # user_count = User.objects.count()  # Total user count
    # revenue = Order.objects.filter(date__month=date.today().month).aggregate(total_revenue=Sum('amount'))['total_revenue'] or 0
    # new_users_today = User.objects.filter(date_joined__date=date.today()).count()

    # # Pass data to the template
    # data = {
    #     'title': 'Dashboard Overview',
    #     'user_count': user_count,
    #     'revenue': revenue,
    #     'new_users': new_users_today,
    # }
    return render(request, 'dashboard/home.html')
def price_view(request):
    
    return render(request, 'dashboard/product_list.html')
