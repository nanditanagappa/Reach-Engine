# reachengine/urls.py
from django.conf.urls import url
from reachengine import views
from django.urls import path

urlpatterns = [
	url('^$', views.HomePageView.as_view()),
	path('about.html', views.AboutPageView.as_view()),
	path('^$', views.get_hashtags, name="fetchHashTag"),
	path('index.html', views.HomePageView.as_view()),
]