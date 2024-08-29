from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register_seller/', views.register_seller, name='register_seller'),
    path('register_buyer/', views.register_buyer, name='register_buyer'),
    path('seller_packages/', views.seller_packages, name='seller_packages'),
    path('packages/', views.available_packages, name='available_packages'),
    path('purchase/<int:package_id>/', views.purchase_package, name='purchase_package'),
    path('purchase_history/', views.purchase_history, name='purchase_history'),
]


