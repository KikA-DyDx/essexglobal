from django.shortcuts import render
from .models import Package

# Currency symbols dictionary
currency_symbols = {
    'USD': '$',
    'ZAR': 'R',
    'EUR': '€',
    'GBP': '£',
}


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def logistics(request):
    return render(request, 'logistics.html')


def contact(request):
    return render(request, 'contact.html')

def international(request):
    return render(request, 'international-freight.html')


def domestic(request):
    return render(request, 'domestic-freight.html')


def forwarder(request):
    return render(request, 'freight-forwarder.html')


def consultation(request):
    return render(request, 'freight-consultation.html')


def household(request):
    return render(request, 'move-household-goods.html')


def commercial(request):
    return render(request, 'ship-commercial-goods.html')


def airfreight(request):
    return render(request, 'air-freight-carrier.html')


def oceanfreight(request):
    return render(request, 'ocean-freight-forwarding.html')


def roadfreight(request):
    return render(request, 'road-freight-forwarding.html')


def socmovements(request):
    return render(request, 'soc-movements.html')


def exportimport(request):
    return render(request, 'export-import.html')


def importersrep(request):
    return render(request, 'importers-logistics-rep.html')


def payment(request):
    return render(request, 'payment.html')

def track_package(request):
    package = None
    error = None
    worth_symbol = ''
    fee_symbol = ''
    tracking_number = request.GET.get('tracking_number')

    if tracking_number:
        try:
            package = Package.objects.get(tracking_number=tracking_number)
            worth_symbol = currency_symbols.get(
                package.shipping_fee_currency, '')
            fee_symbol = currency_symbols.get(
                package.clearance_fee_currency, '')
        except Package.DoesNotExist:
            error = "No package found with this tracking number."

    return render(request, 'track_package.html', {
        'package': package,
        'error': error,
        'worth_symbol': worth_symbol,
        'fee_symbol': fee_symbol
    })
