from django.urls import path
from . import views  # import your views

urlpatterns = [
    path('', views.home, name='home'),
    path('track/', views.track_package, name='track_package'),
    path('about/', views.about, name='about'),
    path('logistics/', views.logistics, name='logistics'),
    path('contact/', views.contact, name='contact'),
    path('international-freight/', views.international, name='international-freight'),
    path('domestic-freight/', views.domestic, name='domestic-freight'),
    path('freight-forwarder/', views.forwarder, name='freight-forwarder'),
    path('freight-consultation/', views.consultation, name='freight-consultation'),
    path('move-household-goods/', views.household, name='move-household-goods'),
    path('ship-comemrcial-goods/', views.commercial, name='ship-commercial-goods'),
    path('air-freight-carrier/', views.airfreight, name='air-freight-carrier'),
    path('ocean-freight-forwarding/', views.oceanfreight, name='ocean-freight-forwarding'),
    path('road-freight-forwarding/', views.roadfreight, name='road-freight-forwarding'),
    path('soc-movements/', views.socmovements, name='soc-movements'),
    path('export-import/', views.exportimport, name='export-import'),
    path('importers-logistics-rep/', views.importersrep, name='importers-logistics-rep'),
    path('payment/', views.payment, name='payment'),
]
