from django.urls import path
from product_app.views import*

urlpatterns = [
    path('',Register, name='Register'),
    path('login_page/',login_page, name='login_page'),
    path('logout_page/',logout_page, name='logout_page'),

    path('dashboard/',dashboard, name='dashboard'),
    path('my-products/',my_products, name='my_products'),
    path('add-product/',add_product, name='add_product'),
    
    path('product-detail/<str:p_id>',product_detail, name='product_detail'),
    path('update-product/<str:p_id>',update_product, name='update_product'),
    path('delete-product/<str:p_id>',delete_product, name='delete_product'),
    
]