from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Site
from django.http import HttpResponseRedirect

# Create your views here.

def scrape(request):
    if request.method == 'POST':
        site = request.POST.get('site')
        page = requests.get(site)
        soup = BeautifulSoup(page.text,'html.parser')

        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            print(f"Link Address: {link_address}, Link Text: {link_text}")
            if link_address is not None:
                Site.objects.create(address=link_address, name=link_text)

        return HttpResponseRedirect('/')
    else:
        data = Site.objects.all()
    
    return render(request,'scrape.html',{'data':data})

def clear(request):
    Site.objects.all().delete()
    return HttpResponseRedirect('/')