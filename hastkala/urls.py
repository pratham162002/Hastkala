"""
URL configuration for hastkala project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings


from django.conf.urls.static import static
from webapp import views as v1




urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',v1.home),
    path('home',v1.web),
    path('add1',v1.web1),
    path('add2',v1.web2),
    path('payments',v1.web3),
    path('4',v1.web4),
    path('extra',v1.web5),
    path('addtocast',v1.web6),
    path('singup',v1.web8),
    path('login',v1.web7),
    path('signsave',v1.signupsave),
    path('loginsave',v1.loginsave),
    
    path('',v1.index),
    
    path('about',v1.About),
    # path('contactnav',v1.contactnav),
    path('contactnav', v1.contact_view),
    # path('home',v1.dashbord),
    
    
    path('product/<int:product_id>/', v1.product_detail, name='product_detail'),
   
    path('add-to-cart/<int:product_id>/', v1.add_to_cart, name='add_to_cart'),
    
   
    path('update-cart-quantity/<int:product_id>/', v1.update_cart_quantity, name='update_cart_quantity'),
    path('remove-from-cart/<int:product_id>/', v1.remove_from_cart, name='remove_from_cart'),
    path('cart/', v1.cart_view, name='cart'),
    path('payments/', v1.payments, name='payments'),
     
    path('payment_page/', v1.payment_page, name='payment_page'),

    # path('payment_page_buynow/', v1.payment_page_buynow, name='payments_page_buynow'),
    
    
    path('process-payment/', v1.process_payment, name='process_payment'),
    
    path('buy-now/<int:product_id>/', v1.buy_now, name='buy_now'),
    path('payment/<int:product_id>/', v1.payment_buynow, name='payment_buynow'),
   
    # ------------------------------------------
    path('payment/<int:product_id>', v1.payment_page_buynow, name='payments_page_buynow'),

    # ==================================================merchant_payment_page
    
     path('merchant-payment/', v1.merchant_payment_page ),
 
    path('generate-qr/<int:product_id>/', v1.generate_qr_code, name='generate_qr'),
    
   path('payment_page/generate_qr_code_card/', v1.generate_qr_code_card, name='generate_qr_code_card'),

    path("save-transaction/", v1.save_transaction, name="save_transaction"),
    
    
     path("submit-comment/", v1.submit_comment, name="submit_comment"),
    path("like-comment/<int:comment_id>/", v1.like_comment, name="like_comment"),

   
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)