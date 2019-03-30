from django.shortcuts import render,redirect
from .models import Category

# Create your views here.


def home(request):
    return render(request, 'crud/home.html')

def form(request):
    return render(request, 'crud/form.html')

def create_data(request):
    category_name = request.POST["category_name"]
    category_description = request.POST["category_description"]
    publication = request.POST["publication"]

    category_info = Category(category_name=category_name, category_description=category_description, publication=publication)
    category_info.save()
    return render(request, 'crud/form.html', {'msg':'created'})


def view_data(request):
    category_view = Category.objects.all()
    return render(request, 'crud/category.html', {'categories': category_view})


def update_data(request,id):
    category_edit = Category.objects.get(id=id)
    return render(request, 'crud/update.html', {'category':category_edit})

def edit_data(request,id):
    category_update = Category.objects.get(id=id)
    category_update.category_name = request.POST["category_name"]
    category_update.category_description = request.POST["category_description"]
    category_update.save()
    return render(request, 'crud/test.html')



def delete_data(request, id):
    category_dlt = Category.objects.get(id=id)
    if request.method == 'POST':
        category_dlt.delete()
        return redirect('view_data')
    return render(request, 'crud/delete-confirm.html', {'category':category_dlt})
