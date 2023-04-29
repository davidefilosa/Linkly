from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from link.models import Link, Category

# Create your views here.

@login_required
def dashboard(request):
    categories = Category.objects.filter(created_by=request.user)
    filter = request.GET.get('filter', '')
    links = Link.objects.filter(created_by=request.user)

    if filter:
        links = links.filter(category_id=filter)

    return render(request, 'dashboard/dashboard.html', {'links': links, 'categories': categories})



