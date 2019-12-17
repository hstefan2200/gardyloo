from django.urls import path, re_path
from main import views as main_views


urlpatterns = [
    path('', main_views.index, name='index'),
    path('learn/', main_views.learn, name='main-learn'),
    path('about/', main_views.about, name='main-about'),
]
