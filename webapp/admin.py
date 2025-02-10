from django.contrib import admin

# Register your models here.
from .models import User,Student,Product,Contact,Payment1,CartItem,Transaction,ContactMessage
admin.site.register(Product)


# admin.site.register(coustmer_detail)

@admin.register(User) 
class useradmin(admin.ModelAdmin):
    list_display=['uname','age','upassword','mobile','address']
    
class Studentadmin(admin.ModelAdmin):
    list_display=['id','name','image']
    
    

class ContactAdmin(admin.ModelAdmin):
    list_display = ('fname', 'address', 'phone', 'email', 'dob')  # Fields displayed in the list view
    search_fields = ('fname', 'email', 'phone')  # Enable search by name, email, or phone
    list_filter = ('dob',)  # Add filter by DOB
    ordering = ('fname',)  # Order by name
    date_hierarchy = 'dob'  # Enable date-based navigation

admin.site.register(Contact, ContactAdmin)


class paymentAdmin(admin.ModelAdmin):
    list_display = ('amount','description','fname', 'address', 'phone', 'email', 'dob')  # Fields displayed in the list view
    search_fields = ('fname', 'email', 'phone')  # Enable search by name, email, or phone
    list_filter = ('dob',)  # Add filter by DOB
    ordering = ('fname',)  # Order by name
    date_hierarchy = 'dob'  # Enable date-based navigation

admin.site.register(Payment1, paymentAdmin)



@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    
    list_display = ('fname','name', 'quantity', 'price', 'created_at','phone', 'email','total_amount')
    list_filter = ('created_at',)
    search_fields = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'quantity', 'price')
        }),
        ('Advanced Options', {
            'fields': ('created_at',),
            'classes': ('collapse',)  # Collapsible section
        }),
    )
    readonly_fields = ('created_at',)  # Make 'created_at' read-only
    
    

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("transaction_id", "name", "phone", "email", "created_at")
    search_fields = ("transaction_id", "name", "email", "phone")
    list_filter = ("created_at",)


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at','message')  # Display these fields in the admin panel
    search_fields = ('name', 'email', 'phone')  # Enable search bar for these fields
    list_filter = ('created_at',)  # Filter messages by submission date
    readonly_fields = ('created_at',)  # Prevent editing of submission timestamp

    fieldsets = (
        ("Customer Info", {'fields': ('name', 'email', 'phone')}),
        ("Message Details", {'fields': ('message',)}),
        ("Timestamp", {'fields': ('created_at',)}),
    )

admin.site.register(ContactMessage, ContactMessageAdmin)