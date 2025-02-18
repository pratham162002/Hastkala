from django.db import models


from django.contrib.auth.models import User
# from django.contrib.auth.models import coustmer_detail

import qrcode




# Create your models here.
class User(models.Model):
    age=models.IntegerField()
    uname=models.CharField(max_length=50)
    upassword=models.CharField(max_length=10)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=50)
    class meta:
        db_table='user'
#========================== product model create=====================================
class addproduct(models.Model):
    price=models.IntegerField()
    pname=models.CharField(max_length=200)
    pimage=models.ImageField(upload_to='img/')
# -------------------------------------------------------
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')  # Requires MEDIA settings to be configured
    stock=models.IntegerField()

    def __str__(self):
        return self.name
    
    
    
    # models.py
class Student(models.Model):
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='img/')
    
    
# ----------------------------------------------------------------------
class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='items/')
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.user.username}"


class Items(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='items/')
    description = models.TextField()

    def __str__(self):
        return self.name


class Payment(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    gst = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=50, choices=(('Pending', 'Pending'), ('Completed', 'Completed')))
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id
    
    # ====================================================
    #                           
#                         merchant_payment_page


class Contact(models.Model):
    fname = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    dob = models.DateField(null=True, blank=True)  # Allow empty values

    def __str__(self):
        return self.fname

# ===========================================================================
# ==================================FOR QR CODE==============================
from django.db import models


class Payment1(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) 
    fname = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    dob = models.DateField(null=True, blank=True)  # Allow empty values
    
    def __str__(self):
        return f"Payment {self.id} - {self.amount}"
    



class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Link to user (optional)
    name = models.CharField(max_length=255)  # Product name
    quantity = models.PositiveIntegerField()  # Quantity of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the item was added


    fname = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    total_amount=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} (x{self.quantity})"
    
    


class Transaction(models.Model):
    transaction_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.transaction_id}"
    
    


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"



# class Comment(models.Model):
#     name = models.CharField(max_length=100)  # Customer's name
#     message = models.TextField()  # Customer's message
#     likes = models.IntegerField(default=0)  # Like count
#     created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

#     def __str__(self):
#         return f"{self.name}: {self.message[:50]}"

    
    
class CustomerQuery(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
    
    
    

class Subscriber(models.Model):
    email = models.EmailField(unique=True)  # Stores emails uniquely
    subscribed_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return self.email