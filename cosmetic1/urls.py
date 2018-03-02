
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('c_user.urls'),name='user'),
    path('cart/', include('c_cart.urls'),name='cart'),
    path('order/', include('c_order.urls'),name='order'),
    path('', include('c_goods.urls'),name='goods'),
]
