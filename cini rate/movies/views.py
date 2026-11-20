from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Movie, Review


def home(request):
    search = request.GET.get('q', '')

    movies = Movie.objects.all().order_by('-id')

    if search:
        movies = movies.filter(title__icontains=search)

    return render(request, 'movies/home.html', {
        'movies': movies,
        'search': search
    })


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    reviews = movie.reviews.all().order_by('-created_at')

    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'reviews': reviews
    })


@login_required
def add_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment', '').strip()

        if rating and rating.isdigit() and comment:
            rating = int(rating)

            if 1 <= rating <= 10:
                Review.objects.create(
                    movie=movie,
                    user=request.user,
                    rating=rating,
                    comment=comment
                )

                average = movie.reviews.aggregate(
                    models.Avg('rating')
                )['rating__avg']

                movie.rating = round(average, 1)
                movie.save()

    return redirect('movie_detail', movie_id=movie.id)

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'movies/register.html', {'form': form})

