from django.urls import path

from .views import *


urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('about/', about, name='about'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('account/', account, name='account'),
    path('<slug:category_slug>', ProductListByCategory.as_view(), name='product_list_by_category'),
    path('<int:id>/<slug:slug>', ProductDetail.as_view(), name='product_detail'),
]
