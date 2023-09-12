from django.shortcuts import render,get_object_or_404
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home(request,c_slug=None):
    c_page=None
    prodt=None
    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        prodt=products.objects.filter(category=c_page,available=True)
    else:

        prodt=products.objects.all().filter(available=True)
    cat=categ.objects.all()
    paginator=Paginator(prodt,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)

    return render(request,'index.html',{'pr':prodt,'ct':cat,'pg':pro})
def prodDetails(request,c_slug,product_slug):
    print("hello")
    try:
        prod=products.objects.get(category__slug=c_slug,slug=product_slug)
        print(prod)
    except Exception as e:
        raise e

    return render(request,'items.html',{'pr':prod})
def searching(request):
    prod=None
    query=None
    if 'Q' in request.GET:
        query=request.GET.get('Q')
        prod=products.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    return render(request,'search.html',{'qr':query,'pr':prod})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            
            pass
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  