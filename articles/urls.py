from django.urls import path
from . import views
app_name='articles'
urlpatterns = [
    path('',views.content,name="list"),
    path('create/',views.create_articles,name='create'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/add/<int:article_id>/', views.add_to_cart,name='add_to_cart'),
    path('cart/remove/<int:article_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('payment_success/',views.payment_success,name='payment_success'),
    path('<slug:slug>/',views.articledetails,name='details'),
    path('checkout/',views.checkout,name='checkout'),
    
   
    
   
]