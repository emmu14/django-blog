from django.shortcuts import render, redirect
from .models import article
from .forms import CreateArticle
from django.contrib.auth.decorators import login_required


def article_list(request):
    articles = article.objects.all().order_by('-date')

    return render(request, 'content.html', {
        'articles': articles
    })


def content(request):
    articles = article.objects.all().order_by('date')

    return render(request, 'content.html', {
        'articles': articles
    })


def articledetails(request, slug):
    article_detail = article.objects.get(slug=slug)

    return render(request, 'article_details.html', {
        'article': article_detail
    })


@login_required(login_url='/accounts/login/')
def create_articles(request):

    if request.method == 'POST':

        form = CreateArticle(request.POST, request.FILES)

        if form.is_valid():

            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()

            return redirect('articles:list')

    else:
        form = CreateArticle()

    return render(request, 'articles/create_article.html', {
        'form': form
    })


def add_to_cart(request, article_id):

    cart = request.session.get('cart', [])

    if article_id not in cart:
        cart.append(article_id)

    request.session['cart'] = cart

    return redirect('articles:cart')

def cart(request):

    cart_ids = request.session.get('cart', [])

    cart_items = article.objects.filter(id__in=cart_ids)

    total = sum(item.price for item in cart_items)

    return render(request, 'articles/cart.html', {
        'cart_items': cart_items,
        'total': total
    })

def checkout(request):

    cart = request.session.get('cart', [])

    cart_items = article.objects.filter(id__in=cart)

    return render(request, 'articles/checkout.html', {
        'cart_items': cart_items
    })


def checkout(request):

    cart = request.session.get('cart', [])

    cart_items = article.objects.filter(id__in=cart)

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')

        return render(request, 'articles/payment.html', {
            'cart_items': cart_items,
            'name': name,
            'email': email,
            'address': address,
        })

    return render(request, 'articles/checkout.html', {
        'cart_items': cart_items
    })

def payment_success(request):
    request.session['cart'] = []

    return render(request, 'articles/payment_success.html')



def remove_from_cart(request, article_id):

    cart_items = request.session.get('cart', [])

    if article_id in cart_items:
        cart_items.remove(article_id)

    request.session['cart'] = cart_items
    request.session.modified = True

    return redirect('articles:cart')