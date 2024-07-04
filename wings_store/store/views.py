from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def Home(request):
    products = Products.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')
        products = products.filter(
            Q(products_name__icontains = search)|
            Q(category__icontains = search)|
            Q(subcategory__icontains = search) |
            Q(price__icontains = search) 

    )
    
    paginator = Paginator(products,4)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    
    params = {'products':products, 'products':page_obj}
    return render(request, "index.html", params)

def Buy(request,id):
    products = Products.objects.get(id=id)
    params = {'products':products}
    return render(request, 'buy.html',params)

def Order(request, id):
    products = Products.objects.get(id=id)
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        selecter = request.POST.get('selecter')
        address = request.POST.get('address')
        contect = Contect.objects.create(fullname=fullname,
                                     email=email,
                                     phone_number=phone_number,
                                     selecter=selecter,
                                     address=address)
        contect.save()
    params = {'products':products}
    return render(request, 'order.html', params)    

def All_Products(request):
    products = Products.objects.all()
    params = {'products':products}
    return render(request, 'products.html',params)