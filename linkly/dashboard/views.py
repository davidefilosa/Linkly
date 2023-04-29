from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from link.models import Link, Category

# Create your views here.

@login_required
def dashboard(request):
    new_links = Link.objects.filter(created_by=request.user)
    categories = Category.objects.filter(created_by=request.user)

    return render(request, 'dashboard/dashboard.html', {'new_links': new_links, 'categories': categories})



