from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Product, Review, ContactMessage

def index(request):
    return redirect('home')

def home(request):
    # Handle contact form submission
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        if name and email and phone and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message
            )
            messages.success(request, 'Thank you! Your message has been sent successfully.')
        else:
            messages.error(request, 'Please fill in all fields.')
        
        return redirect('home')
    
    # Get data for page
    products = Product.objects.all()[:3]  # Show only first 3 products
    reviews = Review.objects.all()[:3]  # Show only first 3 reviews
    
    context = {
        'products': products,
        'reviews': reviews,
    }
    
    return render(request, 'index.html', context)
