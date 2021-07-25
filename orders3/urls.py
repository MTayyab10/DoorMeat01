from django.urls import path
from . import views

app_name = 'orders3'

urlpatterns = [

    # Customer Section

    path('customer/form', views.customer_form, name='customer_form'),
    path('c/response/<int:customer_id>', views.cust_response, name='cust_response'),

    # coupon
    # path('c/response/<int:customer_id>', views.cust_coupon, name='cust_coupon'),
    # path('c/response/<int:customer_id>', views.cust_coupon_update, name='cust_coupon_update'),

    path('c/order_update/<int:customer_id>', views.cust_order_update,
         name='cust_order_update'),

    path('c/order_confirm/<int:customer_id>', views.cust_order_confirm,
         name='cust_order_confirm'),

    path('c/order_delete/<int:customer_id>', views.cust_order_delete,
         name='cust_order_delete'),

    path('c/order/<int:customer_id>', views.order_info, name='order_info'),

    # Butcher Section

    path('butcher/form', views.butcher_form, name='butcher_form'),
    path('b/response/<int:butcher_id>', views.butch_response, name='butch_response'),

    path('b/order_update/<int:butcher_id>', views.butch_order_update,
         name='butch_order_update'),

    path('b_order_delete/<int:butcher_id>', views.butch_order_delete,
         name='butch_order_delete'),

    # Order Info

    path('order_info/<int:user_id>', views.order_info, name='order_info'),

    path('help-center', views.support, name='support')

]
