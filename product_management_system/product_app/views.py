from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from product_app.models import*
from product_app.forms import*

def Register(request):
    form_data = RegisterForm
    if request.method == 'POST':
        form_data = RegisterForm(request.POST)
        
        if form_data.is_valid():
            form_data.save()
            messages.success(request,'Account created successfully')
            return redirect('login_page')
    else:
        messages.warning(request,'User Already Exists')
        form_data = RegisterForm()
        
    context = {
        'form_data':form_data
    }
    
    return render(request, 'auth/Register.html',context)
        
    

def login_page(request):
    form_data = AuthenticationForm()
    if request.method == 'POST':
        form_data = AuthenticationForm(request, data = request.POST)
        
        if form_data.is_valid():
            user = form_data.get_user()
            login(request, user)
            messages.success(request,'Login successfully')
            return redirect('dashboard')
        
    context = {
        'form_data':form_data
    }
        
    return render(request, 'auth/login_page.html',context)

@login_required
def logout_page(request):
    logout(request)
    return redirect('login_page')

@login_required
def dashboard(request):

    products = ProductModel.objects.all()
    search = request.GET.get('search')

    if search:
        products = products.filter(name__icontains=search)
        
    context = {
        'products': products
    }
    return render(request,'pages/dashboard.html',context)

@login_required
def my_products(request):

    products = ProductModel.objects.filter(created_by=request.user)
    category = request.GET.get('category')

    if category:
        products = products.filter(category=category)
        
    context = {
        'products': products
    }
    return render(request,'pages/my_products.html',context)

@login_required
def product_detail(request, p_id):

    product = get_object_or_404(ProductModel, id=p_id)
    
    context ={
        'product': product
    }
    return render(request,'pages/product_detail.html',context)


@login_required
def add_product(request):
    if request.method == 'POST':
        p_data = ProductForm(request.POST,request.FILES)
        if p_data.is_valid():
            product= p_data.save(commit=False)
            product.created_by = request.user
            product.total_amount=product.price * product.qty
            product.save()
            return redirect('my_products')
    else:
        p_data = ProductForm()

        context = {
            'p_data':p_data
        }
        
    return render(request, 'pages/add_product.html',context)

@login_required
def update_product(request,p_id):
    if request.method == 'POST':
        product = ProductModel.objects.get(id = p_id )
        p_data = ProductForm(request.POST,request.FILES,instance = product)
        if p_data.is_valid():
            product= p_data.save(commit=False)
            product.total_amount=product.price * product.qty
            product.save()
            return redirect('my_products')
    else:
        product = ProductModel.objects.get(id = p_id )
        p_data = ProductForm(instance = product)

        context = {
            'p_data':p_data

        }
    return render(request, 'pages/update_product.html',context)

@login_required
def delete_product(request, p_id):
    ProductModel.objects.get(id = p_id).delete()
    return redirect('my_products')

