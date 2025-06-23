from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm
from .forms import SigninForm
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem, Order, Message
from django.shortcuts import get_object_or_404
from django.contrib import messages


# Create your views here.

#---------------------------------home page --------------------------------
def home(request):
    return render(request,'petapp/index.html')


def signup(request):
    if request.method == 'POST':
        print("Received POST request for signup")
        form = SignupForm(request.POST)
        if form.is_valid():
            print("Form is valid. Saving data...")
            form.save()
            # Redirect to signin page
            return redirect('signin')
    else:
        form = SignupForm()
        return render(request, 'petapp/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate user using SigninInfo model
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Login user if authentication is successful
                login(request, user)
                # Redirect to a success page or homepage
                return redirect('home')  # Replace 'home' with the name of your home URL pattern
            else:
                # Authentication failed, display sign-in page with error message
                error_message = "Invalid username or password. Please try again."
                return render(request, 'petapp/signin.html', {'form': form, 'error_message': error_message})
    else:
        form = SigninForm()

    return render(request, 'petapp/signin.html', {'form': form})


def signout(request):
    logout(request)
    # Redirect to a page after logout
    return redirect('home')

@login_required
def profile(request):
    return render(request, 'petapp/profile.html')

def faqs(request):
    return render(request,'petapp/faqs.html')

def message_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Create a new message object and save it to the database
        new_message = Message(name=name, email=email, message=message)
        new_message.save()

        # Redirect to a new URL after successfully saving the message:
        messages.success(request, "A response has been sent.")
        return redirect('home')

    # If the request method is not POST, display the form
    else:
        messages.success(request, "Respond, not send.")
        return render(request, 'petapp/index.html')

#--------------------------------add to cart----------------------------------------------------
def cart(request):
    return render(request,'petapp/cart.html')


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    quantity = int(request.POST.get('quantity', 1))
    cart_item, created = CartItem.objects.get_or_create(product=product, cart=cart)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')


def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = cart.get_total()

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }

    return render(request, 'petapp/cart.html', context)

def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    quantity = int(request.POST.get('quantity', 1))  # get the quantity from the POST data
    cart_item.quantity = quantity
    cart_item.save()
    return redirect('cart')

def empty_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.cartitem_set.all().delete()
    return redirect('cart')

def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    order = Order.objects.create(user=request.user)
    for item in cart.cartitem_set.all():
        item.delete()
    return redirect('order', order_id=order.id)

def order(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'petapp/order.html',{'order': order})
#---------------------------pet page -------------------------------------

def pet(request):
    return render(request, 'petapp/pet.html')

#---------------------------dog ------------------------------------------
def dog(request):
    return render(request, 'petapp/dog.html')

def labrador(request):
    return render(request, 'petapp/labrador.html')

def german(request):
    return render(request, 'petapp/german.html')

def golden(request):
    return render(request, 'petapp/golden.html')

def french(request):
    return render(request, 'petapp/french.html')

def bulldog(request):
    return render(request, 'petapp/bulldog.html')

def boxer(request):
    return render(request, 'petapp/boxer.html')

def husk(request):
    return render(request, 'petapp/husk.html')

#---------------------------cat ------------------------------------------

def cat(request):
    return render(request, 'petapp/cat.html')

def ragdoll(request):
    return render(request, 'petapp/Ragdoll.html')

def coon(request):
    return render(request, 'petapp/coon.html')

def siamese(request):
    return render(request, 'petapp/siamese.html')

def persian(request):
    return render(request, 'petapp/persian.html')

def bengal(request):
    return render(request, 'petapp/bengal.html')

#---------------------------fish ------------------------------------------

def fish(request):
    return render(request, 'petapp/fish.html')

def BettaFish(request):
    return render(request, 'petapp/BettaFish.html')

def Goldfish(request):
    return render(request, 'petapp/Goldfish.html')

def Tetra(request):
    return render(request, 'petapp/Tetra.html')

def Angelfish(request):
    return render(request, 'petapp/Angelfish.html')

def Guppy(request):
    return render(request, 'petapp/Guppy.html')



#---------------------------bird ------------------------------------------

def birds(request):
    return render(request, 'petapp/birds.html')

def parrot(request):
    return render(request, 'petapp/parrot.html')

def lovebird(request):
    return render(request, 'petapp/lovebird.html')

def cockatoo(request):
    return render(request, 'petapp/cockatoo.html')

def cockatiel(request):
    return render(request, 'petapp/cockatiel.html')

def budgerigar(request):
    return render(request, 'petapp/budgerigar.html')

#---------------------------essentials page -------------------------------------

def essentials(request):
    return render(request, 'petapp/essentials.html')


def food(request):
    dog_food = Product.objects.filter(category='dog', subcategory='food')
    cat_food = Product.objects.filter(category='cat', subcategory='food')
    fish_food = Product.objects.filter(category='fish', subcategory='food')
    bird_food = Product.objects.filter(category='bird', subcategory='food')

    context = {
        'dog_food': dog_food,
        'cat_food': cat_food,
        'fish_food': fish_food,
        'bird_food': bird_food,
    }

    return render(request, 'petapp/food.html', context)

def toys(request):
    dog_toys = Product.objects.filter(category='dog', subcategory='toy')
    cat_toys = Product.objects.filter(category='cat', subcategory='toy')
    bird_toys = Product.objects.filter(category='bird', subcategory='toy')

    context = {
        'dog_toys': dog_toys,
        'cat_toys': cat_toys,
        'bird_toys': bird_toys,
    }

    return render(request, 'petapp/toys.html', context)

def furniture(request):
    dog_furniture = Product.objects.filter(category='dog', subcategory='furniture')
    cat_furniture = Product.objects.filter(category='cat', subcategory='furniture')
    fish_furniture = Product.objects.filter(category='fish', subcategory='furniture')
    bird_furniture= Product.objects.filter(category='bird', subcategory='furniture')

    context = {
        'dog_furniture': dog_furniture,
        'cat_furniture': cat_furniture,
        'fish_furniture': fish_furniture,
        'bird_furniture': bird_furniture,
    }

    return render(request, 'petapp/furniture.html', context)


def clothing(request):
    dog_clothing = Product.objects.filter(category='dog', subcategory='clothing')
    cat_clothing= Product.objects.filter(category='cat', subcategory='clothing')
    fish_clothing = Product.objects.filter(category='fish', subcategory='clothing')
    bird_clothing = Product.objects.filter(category='bird', subcategory='clothing')

    context = {
        'dog_clothing': dog_clothing,
        'cat_clothing': cat_clothing,
        'bird_clothing': bird_clothing,
    }

    return render(request, 'petapp/clothing.html', context)

#