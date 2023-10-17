from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, DeleteView
from shop.forms import AddQuantityForm, OrderUserView, FileFormView
from shop.models import Product, Order, OrderItem
from django.views.generic import TemplateView
from .models import auto_payment_unpaid_orders
from django import template
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required

class ProductsListView(ListView):
    model = Product
    template_name = 'shop/shop.html'
    ordering = ["-time"]
    paginate_by = 6 # количество продуктов, которые будут отображаться на странице.
    context_object_name = 'products'
    paginate_by = 6
    
    #количество продуктов, которые будут отображаться на странице.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['load_more'] = self.paginate_by # set the number of products to be loaded
        return context
    
    #Этот код проверяет, есть ли предыдущая страница (), и если она есть, он создает новую кнопку, которая ссылается на первую страницу ().page_obj.has_previous"?page=1&load_more={{ load_more }}"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['load_more'] = self.request.GET.get('load_more', '')
        return context



class ProductsDetailView(DetailView):
    model = Product
    template_name = 'shop/shop-details.html'


@login_required(login_url=reverse_lazy('login'))
def add_item_to_cart(request, pk):
    if request.method == 'POST':
        quantity_form = AddQuantityForm(request.POST)
        if quantity_form.is_valid():
            quantity = quantity_form.cleaned_data['quantity']
            if quantity:
                cart = Order.get_cart(request.user)
                # product = Product.objects.get(pk=pk)
                product = get_object_or_404(Product, pk=pk)
                cart.orderitem_set.create(product=product,
                                          quantity=quantity,
                                          price=product.price)
                cart.save()
                return redirect('shop')
        else:
            pass
    return redirect('shop')


@login_required(login_url=reverse_lazy('login'))
def cart_view(request):
    cart = Order.get_cart(request.user)
    items = cart.orderitem_set.all()
    delivery_form = OrderUserView()
    file_form = FileFormView()
    context = {
        'cart': cart,
        'items': items,
        'form': delivery_form,
        'file_form': file_form,
    }

    if request.method == 'POST':
        cart = Order.get_cart(request.user)
        cart.status = Order.STATUS_WAITING_FOR_PAYMENT
        # доставка
        cart.phone = request.POST.get('phone')  
        cart.location = request.POST.get('location')
        cart.home = request.POST.get('home')
        cart.podezd = request.POST.get('podezd')
        cart.etaj = request.POST.get('etaj')
        cart.kvartir = request.POST.get('kvartir')
        cart.domofon = request.POST.get('domofon')
        cart.comment = request.POST.get('comment')
        # самовывез
        cart.time_samo = request.POST.get('time_samo')
        # if request.FILES:
        #     cart.file = request.FILES['file']
        #email на почту
        send_mail('Новый заказ', str(cart)  + '\n' + 'Доставка:\n' + 'Номер телефона: ' + str(cart.phone) + '\n' + 'Улица: ' + str(cart.location) + 
            '\n' + 'Дом: ' + str(cart.home) + '\n' + 'Подъезд: ' + str(cart.podezd) + '\n' + 'Этаж: ' + str(cart.etaj) + 
            '\n'  + 'Квартира/офис: '  + str(cart.kvartir) + '\n' + 'Комментарий: ' + str(cart.comment) + 
            '\n' + 'Способ оплаты: ' + str(cart.domofon) + '\n' + '\n' + 'Cамовывез:\n'+ 
            '\n' + 'Дата: ' + str(cart.time_samo) + '\n' + '\n' + 'Элемент заказа:\n' + str(items), 'shop.modern.com@gmail.com', ['shop.modern.com@gmail.com'], fail_silently=False)
        # ЭЛЕМЕНТ ЗАКАЗА ПОСМОТРЮ ПОТОМ
        cart.save()
        auto_payment_unpaid_orders(cart.user)
        return redirect('resultat')

    return render(request, 'shop/cart.html', context)



@method_decorator(login_required, name='dispatch')
class CartDeleteItem(DeleteView):
    model = OrderItem
    template_name = 'shop/cart.html'
    success_url = reverse_lazy('cart_view')

    # Проверка доступа
    def get_queryset(self):
        qs = super().get_queryset()
        qs.filter(order__user=self.request.user)
        return qs


@login_required(login_url=reverse_lazy('login'))
def make_order(request):
    cart = Order.get_cart(request.user)
    cart.make_order()
    return redirect('shop')
