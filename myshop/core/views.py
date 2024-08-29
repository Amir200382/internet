
from django.shortcuts import render, redirect
from .forms import SellerRegistrationForm, BuyerRegistrationForm, PackageForm
from .models import Package, Buyer, Seller, Purchase

def register_seller(request):
    if request.method == 'POST':
        form = SellerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Seller.objects.create(user=user)
            return redirect('seller_packages')
    else:
        form = SellerRegistrationForm()
    return render(request, 'core/register_seller.html', {'form': form})

def register_buyer(request):
    if request.method == 'POST':
        form = BuyerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('available_packages')
    else:
        form = BuyerRegistrationForm()
    return render(request, 'core/register_buyer.html', {'form': form})

def seller_packages(request):
    if request.user.is_authenticated and hasattr(request.user, 'seller'):
        packages = Package.objects.filter(seller=request.user.seller)
        if request.method == 'POST':
            form = PackageForm(request.POST)
            if form.is_valid():
                package = form.save(commit=False)
                package.seller = request.user.seller
                package.save()
                return redirect('seller_packages')
        else:
            form = PackageForm()
        return render(request, 'core/seller_packages.html', {'packages': packages, 'form': form})
    else:
        return redirect('register_seller')

def available_packages(request):
    packages = Package.objects.all()
    return render(request, 'core/available_packages.html', {'packages': packages})

def purchase_package(request, package_id):
    package = Package.objects.get(id=package_id)
    buyer = Buyer.objects.first()  
    Purchase.objects.create(buyer=buyer, package=package)
    return redirect('purchase_history')

def purchase_history(request):
    purchases = Purchase.objects.filter(buyer__name="Amir")  
    return render(request, 'core/purchase_history.html', {'purchases': purchases})
