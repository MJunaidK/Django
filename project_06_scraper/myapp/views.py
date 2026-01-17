from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link

# Create your views here.

def scrape(request):
    if request.method == 'POST':
        site = request.POST.get('site')
        if site:
            page = requests.get(site)
            soup = BeautifulSoup(page.content, 'html.parser')

            for link in soup.find_all('a'):
                link_address = link.get('href')
                link_text = link.get_text(strip=True) 

                if not link_text or not link_address:
                    continue

                Link.objects.create(name=link_text, address=link_address)
    
    data = Link.objects.all()
    return render(request, 'myapp/scrape.html', {'data': data})

def clear_links(request):
    Link.objects.all().delete()
    data = Link.objects.all()
    return render(request, 'myapp/scrape.html', {'data': data})

    
