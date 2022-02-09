from rest_framework import routers
from booking import views

router = routers.DefaultRouter()
router.register(r'booking/show-play-list', views.GetPlayListViewSet)
router.register(r'movie/add-play', views.AddMovieViewSet)