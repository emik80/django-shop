from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from orders.models import Order
from .forms import *
from .models import *
from cart.forms import CartAddProductForm
from .utils import DataMixin


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'shop/register.html'
    success_url = reverse_lazy('shop:login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Реєстрація')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('shop:product_list')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'shop/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизація')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('shop:product_list')


def logout_user(request):
    logout(request)
    return redirect('shop:login')


class ProductList(DataMixin, ListView):
    model = Product
    template_name = 'shop/product/list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(available=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Товари')
        return dict(list(context.items()) + list(c_def.items()))


class ProductListByCategory(DataMixin, ListView):
    model = Product
    template_name = 'shop/product/list.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, slug=self.kwargs['category_slug'])

        c_def = self.get_user_context(title=category)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['category_slug'], available=True)


class ProductDetail(DataMixin, DetailView):
    model = Product
    template_name = 'shop/product/detail.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        product = get_object_or_404(Product, id=self.kwargs['id'], slug=self.kwargs['slug'], available=True)
        context['title'] = product
        context['cart_product_form'] = CartAddProductForm()
        return context


def account(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user.id)
        context = {'title': 'Кабінет',
                   'orders': orders,
                   'amount': 0,
                   }
        return render(request, 'shop/account.html', context=context)

    return redirect('shop:login')


def about(request):
    return render(request, 'shop/about.html', {'title': 'Про нас'})
