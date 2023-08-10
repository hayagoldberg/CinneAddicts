from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('movie_detail/<int:movie_id>/', views.movie_detail_view, name='movie_detail'),
]
