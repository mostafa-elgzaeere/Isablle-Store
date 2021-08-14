from django import forms
from django.shortcuts import render
from .models import Categorie ,Product ,Comment
from cart.forms import ProductForm
from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.

def home(request,name_categorey=None):
    form= ProductForm()
    categories=Categorie.objects.all()
    products=Product.objects.filter(active=True)
    current_categorey=None
    if name_categorey:
        current_categorey=Categorie.objects.get(name=name_categorey)
        products=Product.objects.filter(categorey=current_categorey,active=True)
        paginator = Paginator(products, 5) 

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    
    paginator = Paginator(products, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'home.html',{"categories":categories,"products":page_obj,"current_categorey":current_categorey,"form":form})



def product_detil(request,product_choice):
    form= ProductForm()
    product=Product.objects.get(id=product_choice,active=True)
    comments=Comment.objects.filter(product__id=product_choice)

    if request.method == "POST":
        user=request.user
        content=request.POST.get("content")
        c=Comment(
            writer=user,
            content=content,
            product=product
        )
        c.save()
    return render(request,"product_detail.html",{"product":product,"form":form,"comments":comments})

