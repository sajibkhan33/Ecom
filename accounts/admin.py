from django.contrib import admin

# Register your models here.
from .models import CartItems, Profile , Cart

admin.site.register(Profile)

admin.site.register(Cart)
admin.site.register(CartItems)