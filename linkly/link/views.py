from django.shortcuts import render, redirect
from .forms import CategoryForm, LinkForm
from django.contrib.auth.decorators import login_required
from .models import Category, Link
# Create your views here.

@login_required
def links(request):
    links = Link.objects.filter(created_by=request.user)
    return render(request, 'link/links.html', {'links': links})



@login_required
def categories(request):
    categories = Category.objects.filter(created_by=request.user)
    return render(request, 'link/categories.html', {'categories': categories})



@login_required
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.created_by = request.user
            category.save()
            return redirect('/dashboard/')
    else:
        form = CategoryForm()
        return render(request, 'link/create_category.html', {'form': form})



@login_required
def edit_category(request, pk):
    category = Category.objects.get(id=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
            category = form.save(commit=False)
            category.created_by = request.user
            category.save()
            return redirect('/dashboard/')
    else:
        form = CategoryForm(instance=category)
        return render(request, 'link/edit_category.html', {'form': form})



@login_required
def delete_category(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect('/dashboard/')




@login_required
def add_link(request):
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.created_by = request.user
            link.save()
            return redirect('/dashboard/')
    else:
        form = LinkForm()
        form.fields['category'].queryset = Category.objects.filter(created_by=request.user)
        return render(request, 'link/create_link.html', {'form': form})


@login_required
def edit_link(request, pk):
    link = Link.objects.get(id=pk)
    form = LinkForm(request.POST or None, instance=link)
    if form.is_valid():
            link = form.save(commit=False)
            link.created_by = request.user
            link.save()
            return redirect('/dashboard/')
    else:
        form = LinkForm(instance=link)
        return render(request, 'link/edit_link.html', {'form': form})









@login_required
def delete_link(request, pk):
    category = Link.objects.get(id=pk)
    category.delete()
    return redirect('/dashboard/')