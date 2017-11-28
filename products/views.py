from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404

# Create your views here.
def get_index(request):
    return render(request, 'index.html')
    
def all_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})
    
def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {'products': products})
    
def product_detail(request):
    this_product = get_object_or_404(request, pk=id)
    return render(request, "product_detail.html", {"product": this_product})