from django.contrib import admin

from .models import Discount


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('coupon', ('cpn_id'))


admin.site.register(Discount, DiscountAdmin)