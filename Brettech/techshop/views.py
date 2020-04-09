from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def bread(request):
    return render(request, 'bread.html')


def checkout(request):
    return render(request, 'checkout.html')


def drinks(request):
    return render(request, 'drinks.html')


def events(request):
    return render(request, 'events.html')


def faqs(request):
    return render(request, 'faqs.html')


def frozen(request):
    return render(request, 'frozen.html')


def household(request):
    return render(request, 'household.html')


def kitchen(request):
    return render(request, 'kitchen.html')


def login(request):
    return render(request, 'login.html')


def mail(request):
    return render(request, 'mail.html')


def payment(request):
    return render(request, 'payment.html')


def pet(request):
    return render(request, 'pet.html')


def privacy(request):
    return render(request, 'privacy.html')


def products(request):
    return render(request, 'products.html')


def services(request):
    return render(request, 'services.html')


def shortcodes(request):
    return render(request, 'short-codes.html')


def single(request):
    return render(request, 'single.html')


def vegetables(request):
    return render(request, 'vegetables.html')
