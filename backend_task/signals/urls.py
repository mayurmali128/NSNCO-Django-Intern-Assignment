from django.urls import path
from .views import WorkList, ArtistWorkList, RegisterUser


urlpatterns = [
    path('api/works', WorkList.as_view(), name='work-list'),
    path('api/works-by-artist', ArtistWorkList.as_view(), name='artist-work-list'),
    path('api/register', RegisterUser.as_view(), name='register'),
]
