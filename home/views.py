from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Product
import logging
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer



logger = logging.getLogger(__name__)


# Create your views here.

def index(request):
   # return HttpResponse("This is homepage")
   #context is set of variables(dictionary) that you will send into template
   context={
      
       #we will fetch the data from databae or fetch date of blof etc here to give it to template
       'variable':"value of my first variable",     #this variable is called in index.html template
       'variable2':"value of my second variable"
   }
   return render(request,'index.html',context)


def about(request):
     logger.info("🧠 Someone visited the About page!")  # This is our test log. 
    #return HttpResponse("This is about")
     return render(request,'about.html')

def services(request):
    #return HttpResponse("This is service")
    return render(request,'services.html')

def contact(request):
    #return HttpResponse("This is contact")
    if request.method=='POST':
    #it means that if anyone pot form then it will run only otherwise not.
       name=request.POST.get('name')
       email=request.POST.get('email')
       phone=request.POST.get('phone')
       contact=Contact(name=name , email=email ,phone=phone , date=datetime.today())
       contact.save()
       messages.success(request, "Your messsage has been sent!") #for displaying  this message go in base.html after navbar.This command is from website https://docs.djangoproject.com/en/5.2/ref/contrib/messages/
    return render(request,'contact.html')


def ice_cream_view(request):
    items = Product.objects.filter(category='ice-cream')
    return render(request, 'services_list.html', {'items': items, 'title': 'Ice Cream'})

def softy_view(request):
    product_list = Product.objects.filter(category='softy')
    paginator = Paginator(product_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'services_list.html', {
        'page_obj': page_obj,
        'title': 'Softy'
    })


def family_pack_view(request):
    items = Product.objects.filter(category='family-pack')
    return render(request, 'services_list.html', {'items': items, 'title': 'Family Pack'})

# Optional: Add to Cart (Simple Session-Based)
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    #return redirect(request.META.get('HTTP_REFERER', '/'))
    return redirect('view_cart') 



def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after signup
            return redirect('index')  # Change as per your homepage
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})





# Replace your existing services view with this:
@login_required
def services(request):
    return render(request, 'services.html')



def add_to_cart(request, item_id):
    cart = request.session.get('cart', {})
    cart[item_id] = cart.get(item_id, 0) + 1  # Increment quantity
    request.session['cart'] = cart
    messages.success(request, 'Item added to cart.')
    return redirect('cart')

def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0
    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total = product.price * quantity
        cart_items.append({'product': product, 'quantity': quantity, 'total': total})
        total_price += total

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })

def checkout_view(request):
    if request.method == 'POST':
        request.session['cart'] = {}  # Clear cart after checkout
        messages.success(request, 'Order placed successfully!')
        return redirect('order_placed')
    return render(request, 'checkout.html')

def order_placed_view(request):
    return render(request, 'order_placed.html')







from .serializers import ProductSerializer
from rest_framework import generics

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer











