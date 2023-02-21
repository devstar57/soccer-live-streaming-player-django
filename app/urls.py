from django.urls import re_path
from . import views
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^get_player_data$', views.get_player_data, name='get_player_data'),
]
