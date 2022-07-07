from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

from listings.models import Band


def hello(request):     # function not used replaced by band_list
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})


from django.shortcuts import get_object_or_404


def band_detail(request, id):
    band = Band.objects.get(id=id)
    # band = get_object_or_404(Band, id) # we can throw error 404 if id is not in db !
    return render(request, 'listings/band_detail.html', {'band': band})


from listings.forms import BandForm


def band_create(request):
    if request.method == "POST":
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()

    return render(request, 'listings/band_create.html', {'form': form})


def band_update(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(request, 'listings/band_update.html', {'form': form})


def band_delete(request, id):
    band = Band.objects.get(id=id)
    if request.method == "POST":
        band.delete()
        return redirect('band-list')
    return render(request, 'listings/band_delete.html', {'band': band})


def about(request):
    # return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch!</p>')
    return render(request, 'listings/about.html')


from listings.models import Listing


def listings_list(request):
    all_listings = Listing.objects.all()
    return render(request, 'listings/listings-list.html', context={'listings': all_listings})


def listings_detail(request, id):
    elem = Listing.objects.get(id=id)
    return render(request, 'listings/listing_detail.html', {'elem': elem})


from listings.forms import ListingForm


def listings_add(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect('listings-detail', listing.id)
    else:
        form = ListingForm()
    return render(request, 'listings/listing_create.html', {'form': form})


def listing_update(request, id):
    listing = Listing.objects.get(id=id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listings-detail', listing.id)
    else:
        form = ListingForm(instance=listing)
    return render(request, 'listings/listing_update.html', {'form': form})


def listing_delete(request, id):
    listing = Listing.objects.get(id=id)
    if request.method == 'POST':
        listing.delete()
        return redirect('listings-list')
    return render(request, 'listings/listing_delete.html', {'listing': listing})


from listings.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect


def contact(request):
    #return HttpResponse('<h1>Contact us </h1> <p>Mail adress + phone number !</p>')

    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz']
            )
            return redirect('email-sent')
    else:   # GET case
        form = ContactUsForm()

    return render(request, 'listings/contact.html', {'form': form})


def email_sent(request):
    return render(request, 'listings/email_sent.html')

