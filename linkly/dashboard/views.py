from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from link.models import Link

# Create your views here.

@login_required
def dashboard(request):
    new_links = Link.objects.filter(created_by=request.user).order_by('-created_at')[0:5]
    return render(request, 'dashboard/dashboard.html', {'new_links': new_links})
