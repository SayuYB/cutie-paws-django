from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # home page urls--------------------------------
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('profile/', profile, name='profile'),
    path('faqs/', faqs, name='faqs'),
    path('message_view/', message_view, name='message_view'),

    # add to cart------------------------------------------------------------
    path('cart/', cart, name='cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('update_cart/<int:item_id>/', update_cart, name='update_cart'),
    path('empty_cart/', empty_cart, name='empty_cart'),
    path('order/<int:order_id>/', order, name='order'),
    path('checkout/', checkout, name='checkout'),

    # pet page urls---------------------------------
    path('pet/', pet, name='pet'),

    #dog page----------------------------------------
    path('dog/', dog, name='dog'),
    path('labrador/', labrador, name='labrador'),
    path('german/', german, name='german'),
    path('golden/', golden, name='golden'),
    path('french/', french, name='french'),
    path('bulldog/', bulldog, name='bulldog'),
    path('boxer/', boxer, name='boxer'),
    path('husk/', husk, name='husk'),

    #cat page-------------------------------------
    path('cat/', cat, name='cat'),
    path('ragdoll/', ragdoll, name='ragdoll'),
    path('coon/', coon, name='coon'),
    path('siamese/', siamese, name='siamese'),
    path('persian/', persian, name='persian'),
    path('bengal/', bengal, name='bengal'),

    #fish page-------------------------------------
    path('fish/', fish, name='fish'),
    path('BettaFish/', BettaFish, name='BettaFish'),
    path('Goldfish/', Goldfish, name='Goldfish'),
    path('Tetra/', Tetra, name='Tetra'),
    path('Angelfish/', Angelfish, name='Angelfish'),
    path('Guppy/', Guppy, name='Guppy'),

    #bird page-------------------------------------
    path('birds/', birds, name='birds'),
    path('parrot/', parrot, name='parrot'),
    path('lovebird/', lovebird, name='lovebird'),
    path('cockatoo/', cockatoo, name='cockatoo'),
    path('cockatiel/', cockatiel, name='cockatiel'),
    path('budgerigar/', budgerigar, name='budgerigar'),

    #essentials page--------------------------------
    path('essentials/', essentials, name='essentials'),

    path('food/', food,name='food'),
    path('toys/', toys,name='toys'),
    path('furniture/', furniture,name='furniture'),
    path('clothing/', clothing,name='clothing'),

]