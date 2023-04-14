from django.db import models




# Create your models here 
# just creating a timestamp edit 12:36 4/15/2023

class promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    #product_set (reverse relationship created by django)

class collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('product',on_delete=models.SET_NULL,null=True,related_name='+') # + sign is used to dictate that there is no need to create a reverse relationship to django

class product(models.Model):
    # you can create a primary key yourself using below comment.
    # sku = models.CharField(max_length=10,primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(collection,on_delete=models.PROTECT)
    # promotions = models.ManyToManyField(promotion, related_name='products')
    promotions = models.ManyToManyField(promotion)

class customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE,'Bronze'),
        (MEMBERSHIP_SILVER,'Silver'),
        (MEMBERSHIP_GOLD,'Gold'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=25)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES)
    # order = models.ForeignKey('order',on_delete=models.CASCADE,related_name='')   not needed



class order(models.Model):
    
    PAYMENT_PENDING = 'p'
    PAYMENT_COMPLETE = 'C'
    PAYMENT_FAILED = 'F'

    PAYMENT_STATUS_TYPES = [
        (PAYMENT_PENDING,"Pending"),
        (PAYMENT_COMPLETE,"Complete"),
        (PAYMENT_FAILED,"Failed"),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1,choices=PAYMENT_STATUS_TYPES,default=PAYMENT_PENDING)
    customer = models.ForeignKey(customer, on_delete=models.PROTECT)

class order_item(models.Model):

    order = models.ForeignKey(order,on_delete=models.PROTECT)
    product = models.ForeignKey(product,on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10,decimal_places=2)

class address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=15,null=True)

    #  below comment shows one to one relationship between customer and address
    # customer = models.OneToOneField(customer,on_delete=models.CASCADE,primary_key=True)
    customer = models.ForeignKey(customer,on_delete=models.CASCADE)

class cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class cartItem(models.Model):
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    # you can use string 'product' ^ here instead of directly calling it as well
    quantity = models.PositiveSmallIntegerField()

