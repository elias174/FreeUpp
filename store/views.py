# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, JsonResponse

from .forms import ProductForm
from .models import Product, Category


def index(request):
    products = Product.objects.all().order_by('timestamp')
    return render(request, 'index.html', {'products': products})


def category_products(request, pk):
    products = Product.objects.filter(category=pk).order_by('timestamp')
    return render(request, 'index.html', {'products': products})


@login_required
@csrf_exempt
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.company = request.user
            product.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


def detail_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'detail_product.html', {'product': product})

@csrf_exempt
def get_categories(request):
    categories = Category.objects.all().values_list('id', 'name')
    return JsonResponse({'categories': list(categories)})