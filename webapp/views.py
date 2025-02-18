from django.shortcuts import render,redirect, get_object_or_404
# from django.http import HttpResponse
from django.http import JsonResponse

from .models import User,Product,Item,Cart,Contact, CartItem,Transaction,ContactMessage



from django.template.defaulttags import register
from email.mime import image

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

import base64
import qrcode
import uuid
from io import BytesIO

from reportlab.pdfgen import canvas

from django.core.files.storage import FileSystemStorage

from django.http import FileResponse


from django.core.exceptions import ValidationError
from django.http import JsonResponse 
from datetime import datetime
from django.core.files.base import ContentFile

from django.views.decorators.csrf import csrf_exempt
import json

from django.conf import settings
from .models import Payment1

from django.core.files import File
from django.contrib import messages

# Create your views here.
# def home (req):
#     return HttpResponse("hello world")
def web(req):
    return render(req,'w.html')

def web1(req):
    return render (req,'add1.html')

def web2(req):
    return render(req,'circles.html')

def web3(req):
    return render (req,'payments.html')

def web4(req):
    return render (req,'4page.html')

def web5(req):
    return render (req,'extra.html')

def web6 (req):
    return render (req,'addtocast.html')

def web7(req):
    
    return render(req,'login.html')

def web8(req):
    return render(req,'singup.html')

def dashbord(req):
    return render(req,'dashbord.html')

def About (req):
    return render(req,'about.html')

# def contactnav(req):
#     return render(req,'contactnav.html')


def index(req):
    return render (req,'index.html')



def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        

        # Save data to the database
        ContactMessage.objects.create(name=name, email=email, phone=phone, message=message)

        # return redirect('contact_success')  # Redirect to a success page

    return render(request, 'contactnav.html')




def signupsave(req):
    obj=User()
    obj.uname=req.POST.get('uname')
    obj.age=req.POST.get('age')
    obj.upassword=req.POST.get('upass')
    obj.mobile=req.POST.get('umobile')
    obj.address=req.POST.get('uaddress')
    obj.save()
    # return  redirect ('/')
    return redirect('/login')

def loginsave(req):
    uname=req.POST.get('unm')
    upassword=req.POST.get('pwd')
    record=User.objects.filter(uname=uname,upassword=upassword) 
    if(record):
        listData=record.values()
        uid=listData[0]['id']
        uname=listData[0]['uname'] 
        req.session['uid']=uid 
        req.session['uname']=uname
        return render(req,'w.html')
    else:
        return render(req,'login.html',{'Error':'invaild choice'})
   
#    ----------------------------- 
    
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})





# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     cart = request.session.get('cart', [])

#     # Check if product already exists in the cart
#     for item in cart:
#         if item['id'] == product.id:
#             item['quantity'] = item.get('quantity', 1) + 1  # Increment quantity
#             break
#     else:
#         # Add product to cart if not already present
#         cart.append({
#             'id': product.id,
#             'name': product.name,
#             'image':product.image,
#             'price': float(product.price),
#             'quantity': 1
#         })

#     request.session['cart'] = cart
#     request.session.modified = True
#     return redirect('cart')





def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', [])

    # Check if product already exists in the cart
    for item in cart:
        if item['id'] == product.id:
            item['quantity'] = item.get('quantity', 1) + 1
            break
    else:
        # Add product to cart if not already present
        cart.append({
            'id': product.id,
            'name': product.name,
            'image': product.image.url if product.image else '/static/images/default.png',  # Pass the image URL
            'price': float(product.price),
            'quantity': 1
        })

    request.session['cart'] = cart
    request.session.modified = True
    return redirect('cart')

#  Update Quantity View
def update_cart_quantity(request, product_id):
    cart = request.session.get('cart', [])
    action = request.POST.get('action')

    for item in cart:
        if item['id'] == product_id:
            if action == 'increase':
                item['quantity'] += 1
            elif action == 'decrease':
                if item['quantity'] > 1:
                    item['quantity'] -= 1
                else:
                    cart.remove(item)  # Remove product if quantity is 0
            elif action == 'remove':
                cart.remove(item)
            break

    request.session['cart'] = cart
    request.session.modified = True
    return redirect('cart')




# Add a remove_from_cart function to handle the removal of items from the cart

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', [])

    # Filter out the item with the given product_id
    cart = [item for item in cart if item['id'] != product_id]

    # Save the updated cart back to session
    request.session['cart'] = cart
    request.session.modified = True
    return redirect('cart')  # Redirect back to the cart page





# Add Helper Function for Total
@register.filter
def sum_total(cart):
    return sum(item['price'] * item['quantity'] for item in cart)



def product_list(request):
    products = [
          {"id": 1, "name": "Black & Gold Palm Print", "price": 2999, "image": "images/gift3.png"},
          {"id": 2, "name": "Elegant Vase", "price": 1599, "image": "images/vase.png"},
        
    ]
    return render(request, 'w.html', {'products': products})


def payments(request):
    return render(request, 'payments.html')  # Ensure 'payments.html' exists in your templates folder
    
# ----------------------------------------------------------------------------------cast





def cart_view(request):
    # Get cart data from the session
    cart = request.session.get('cart', [])

    # Add product_id to each item in the cart (if not already present)
    for item in cart:
        if 'product_id' not in item:
            item['product_id'] = item.get('id', None)  # Use 'id' or any other unique identifier
        item['total_price'] = item['price'] * item['quantity']

    total_price = sum(item['total_price'] for item in cart)

    # Handle coupon code
    discount = 0
    coupon_code = request.POST.get('coupon_code', '').strip()
    if coupon_code == "newhastkala":
        discount = total_price * 0.5  # 50% discount
        request.session['discount'] = discount  # Save discount to session
        request.session['coupon_code'] = coupon_code  # Save coupon code for reference
        total_price -= discount
    else:
        request.session['discount'] = 0  # No discount
        request.session['coupon_code'] = ''  # Reset coupon code

    request.session.modified = True  # Mark session as modified
    return render(request, 'cart.html', {
        'cart': cart,
        'total_price': total_price,
        'discount': discount,
        'coupon_applied': coupon_code == "newhastkala"
    })


def home_view(request):
    cart = request.session.get('cart', [])
    return render(request, 'home.html', {'cart': cart})



# ---------------------------------------------------------------------
  # Ensure the user is logged in before accessing the payment page
def payment_page(request):
    # Fetch cart items and discount from the session
    
    cart = request.session.get('cart', [])
    discount = request.session.get('discount', 0)

    total_price = sum(item['price'] * item['quantity'] for item in cart)
    gst = total_price * 0.18  # Example: 18% GST
    shipping_charge = total_price * 0.3  # Example: 30% shipping charge

    # Apply discount before calculating grand total
    grand_total = total_price + gst + shipping_charge - discount

    context = {
        'cart': cart,
        'total_price': total_price,
        'discount': discount,
        'gst': gst,
        'shipping_charge': shipping_charge,
        'grand_total': grand_total,
    }
    return render(request, 'payment_page.html', context)






@login_required
def process_payment(request):
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        # Handle payment logic here (e.g., integrate with a payment gateway)
        return HttpResponse(f"Payment successful with {payment_method}")
    return redirect('cart')


# # ---------------------------------------------------


def buy_now(request, product_id):
    # Get the product from the database
    product = get_object_or_404(Product, id=product_id)
    
    # Calculate GST and total price
    gst = product.price * 0.18  # Assuming 18% GST
    total_price = product.price + gst
    
    # Pass details to the template
    context = {
        'product': product,
        'gst': gst,
        'total_price': total_price,
    }
    return render(request, 'buy_now.html', context)




def payment_buynow(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
   
    context = {
        'product': product,
       
    }
    return render(request, 'payment_buynow.html', context)

# -----------------------------------------------------------------------------------
#                           after buynow payment page


from decimal import Decimal


def payment_page_buynow(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    gst_rate = Decimal('0.13')  # GST rate (13%)
    shipping_rate = Decimal('0.13')  # Shipping rate (30%)

    gst = product.price * gst_rate
    shipping_charge = product.price * shipping_rate
    total_price = product.price + gst + shipping_charge

    context = {
        'product': product,
        'gst': gst,
        'total_price': total_price,
        'shipping_charge': shipping_charge,  # Updated variable name
    }
    return render(request, 'payment.html', context)


# ====================================================================
#                                        merchant_payment_page

# =====================save coustermer details==========================

# ==========================



#                          [buy now page qr]
def generate_qr_code(request,product_id):
    if request.method == 'POST':
        # product = get_object_or_404(Product,product_)
        product = get_object_or_404(Product, id=product_id)
        
        
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        fname = request.POST.get('fname')
        address=request.POST.get('address')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # Create a payment record
        payment = Payment1.objects.create(amount=amount, description=description,fname=fname,address=address,email=email,phone=phone) 
 
        # Generate UPI payment link
        upi_id = "prathamsahu3@ybl"  # Replace with your UPI ID
        recipient_name = "pratham "  # Replace with your name
        upi_link = f"upi://pay?pa={upi_id}&pn={recipient_name}&am={amount}&cu=INR"

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(upi_link)  # Add UPI payment link to QR code
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')

        # Save QR code to the payment model
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        payment.qr_code.save(f'qr_code_{payment.id}.png', File(buffer), save=True)
        buffer.close()
        context={
            'payment':payment,
            # 'product':product
        }
        
        if request.method == 'POST':
            fname = request.POST.get('fname', '')
            address = request.POST.get('address', '')
            phone = request.POST.get('phone', '')
            email = request.POST.get('email', '')
            dob = request.POST.get('dob', '')

            # Handle empty DOB
            if dob:
                try:
                    dob = datetime.strptime(dob, "%Y-%m-%d").date()
                except ValueError:
                    return JsonResponse({"error": "Invalid date format. Use YYYY-MM-DD."}, status=400)
            else:
                dob = None  # Allow null value

            # Save contact to the database
            contact = Contact(fname=fname, address=address, phone=phone, email=email, dob=dob)
            contact.save()
        return render(request, 'payment_qr.html', context)
    
    product = get_object_or_404(Product, id=product_id)
    gst_rate = Decimal('0.13')  # GST rate (13%)
    shipping_rate = Decimal('0.13')  # Shipping rate (30%)

    gst = product.price * gst_rate
    shipping_charge = product.price * shipping_rate
    total_price = product.price + gst + shipping_charge
    context = {
        'product': product,
        'gst': gst,
        'total_price': total_price,
    }
    return render(request, 'generate_qr.html',context)

#                    [views page qr]



def generate_qr_code_card(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address', '')
        dob = request.POST.get('dob', '')

        # Create a payment record
        payment = Payment1.objects.create(
            amount=amount,
            fname=fname,
            email=email,
            phone=phone
        )

        # Generate UPI link
        upi_id = "prathamsahu3@ybl"  # Use your new UPI ID
        recipient_name = "Pratham"  # Use your name
        upi_link = f"upi://pay?pa={upi_id}&pn={recipient_name}&am={amount}&cu=INR"

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(upi_link)  # Only add the UPI link to the QR code
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')

        # Save QR code to the payment model
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        payment.qr_code.save(f'qr_code_{payment.id}.png', File(buffer), save=True)
        buffer.close()

        # Handle empty DOB
        if dob:
            try:
                dob = datetime.strptime(dob, "%Y-%m-%d").date()
            except ValueError:
                return JsonResponse({"error": "Invalid date format. Use YYYY-MM-DD."}, status=400)
        else:
            dob = None  # Allow null value

        # Save contact to the database
        contact = Contact(fname=fname, address=address, phone=phone, email=email, dob=dob)
        contact.save()

        # Save cart items to the database
        cart = request.session.get('cart', [])
        for item in cart:
            CartItem.objects.create(
                total_amount=amount,
                fname=fname,
                email=email,
                phone=phone,
                name=item['name'],
                quantity=item['quantity'],
                price=item['price'],
            )

        return render(request, 'payment_view_qr.html', {'payment': payment})

    # Handle GET request
    cart = request.session.get('cart', [])
    discount = request.session.get('discount', 0)
    total_price = sum(item['price'] * item['quantity'] for item in cart)
    gst = total_price * 0.18  # Example: 18% GST
    shipping_charge = total_price * 0.3  # Example: 30% shipping charge

    # Apply discount before calculating grand total
    grand_total = total_price + gst + shipping_charge - discount

    context = {
        'cart': cart,
        'total_price': total_price,
        'discount': discount,
        'gst': gst,
        'shipping_charge': shipping_charge,
        'grand_total': grand_total,
    }

    return render(request, 'generatecard_qr.html', context)

def save_transaction(request):
    if request.method == "POST":
        transaction_id = request.POST.get("transaction_id")
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")

        # Save transaction to the database
        Transaction.objects.create(
            transaction_id=transaction_id,
            name=name,
            phone=phone,
            email=email
        )

        return JsonResponse({"success": True})  # Send response to frontend

    return JsonResponse({"success": False, "message": "Invalid request"})


# -------------------- footer comment box 

# from .models import Comment

# def comment_view(request):
#     if request.method == "POST":
#         name = request.POST.get('name')  # Get customer's name
#         message = request.POST.get('message')  # Get customer's message
        
#         if name and message:  # Ensure both fields are filled
#             Comment.objects.create(name=name, message=message)  # Save to database
#             return redirect('comment_view')  # Refresh the page

#     comments = Comment.objects.all().order_by('-created_at')  # Fetch all comments
#     return render(request, 'w.html', {'comments': comments})
# ---------------------------------------------------------
#                               help page

from .models import CustomerQuery


def submit_query(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        CustomerQuery.objects.create(name=name, email=email, message=message)


        return redirect('submit_query')  # ✅ Redirect to Help Page

    return render(request, "help.html")



from .models import Subscriber

def subscribe(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if email:
            if not Subscriber.objects.filter(email=email).exists():  # Avoid duplicates
                Subscriber.objects.create(email=email)
                return JsonResponse({"status": "success", "message": "Subscribed successfully!"})
            else:
                return JsonResponse({"status": "error", "message": "Email already subscribed."})
    return JsonResponse({"status": "error", "message": "Invalid request."})
