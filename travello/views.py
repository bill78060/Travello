from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Destination
from .forms import DestinationForm
from django.contrib import messages

def homepage(request):
    destinations = Destination.objects.all()
    return render(request, 'index.html', {'destinations': destinations})

import logging
logger = logging.getLogger(__name__)

def dest_details(request, dest_id):
    dest = Destination.objects.filter(id=dest_id).first()
    if dest:
        d = request.COOKIES.setdefault('recent_destinations', '')
        if dest.name not in d.split('\n'):
            d = d + '\n' + dest.name
            d = d.strip('\n')
        logger.info(f"Recent Destinations Cookie: {d}")
        response = render(request, 'destination.html', {'destination': dest})
        response.set_cookie('recent_destinations', d)
        return response
    else:
        messages.error(request, "Destination not found")
        return redirect('/')

def clear_cookies_view(request):
    response = HttpResponse("Clearing cookies")
    if 'recent_destinations' in request.COOKIES:
        response.delete_cookie('recent_destinations')
        print(response)
    return response

def dest_add(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            messages.error(request, 'Error while creating Destination')
    else:
        form = DestinationForm()
    return render(request, 'destinationForm.html', {'form': form})
