from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Comment
from .forms import CommentForm


# Create your views here.


def index_view(request):
    movies = Movie.objects.all()
    return render(request, 'website/index.html', {'movies': movies, 'user': request.user})


def movie_detail_view(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    comments = Comment.objects.filter(movie=movie)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
            return redirect('website:movie_detail', movie_id=movie_id)
    else:
        form = CommentForm()

    context = {'movie': movie, 'comments': comments, 'form': form}
    return render(request, 'website/movie_info.html', context)

