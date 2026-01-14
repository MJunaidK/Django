from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Movie

# Create your views here.

def movie_list(request):
    movie_objects = Movie.objects.all()

    search_query = request.GET.get('search')
    if search_query != None and search_query is not None:
        movie_objects = movie_objects.filter(name__icontains=search_query)

    paginator = Paginator(movie_objects, 4)  # Show 4 movies per page
    page = request.GET.get('page')
    movie_objects = paginator.get_page(page)
    return render(request, 'newapp/movie_list.html', {'movie_objects': movie_objects})
