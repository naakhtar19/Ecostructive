from django.contrib import admin
from stellarapp.models import Orders

# Register your models here.
class OrdersAdmin(admin.ModelAdmin):
    pass
admin.site.register(Orders, OrdersAdmin)

